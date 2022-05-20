from flask import request
from flask_restplus import Resource
from ..util.dto import WFDto
from ruamel.yaml import YAML
import cwl_utils.parser_v1_2 as cwl
import json
import os

api = WFDto.api

@api.route('/')
class Serialize(Resource):

# Get workflow from request
    # Input example:
    # {"0":[{"modelId":"M1","inputs":["a","b","c"],"outputs":["d","e"]}],"1":[{"modelId":"M2","inputs":["a","d"],"outputs":["f"]},{"modelId":"M3","inputs":["b","d"],"outputs":["g","h"]},{"modelId":"M8","inputs":["a","d"],"outputs":["y"]}],"2":[{"modelId":"M5","inputs":["e","f","g"],"outputs":["z"]}]}
    # Key - Step
    # Value - Set of models
    # Model related to ontology? data properties
# For every key in the hashmap
    # For every model in the "Value"
        # Create a Step in CWL
        # Set Step-Output to model's output file
        # Set baseCommand to curl, and url to to model's url
        # Set stdout to save output to file
# Define workflow output based on steps' output
    @api.doc('Serialize a workflow')
    @api.response(200, 'The request was received succesfully')
    @api.response(500, 'Internal error occured')
    @api.expect(WFDto.serializeModel)
    def put(self):
        """Serialize a workflow as CWL"""

        CONTENTTYPE="Content-Type: "
        AUTH="Authorization: "

        print("Serializer: Start")

        if not request.is_json:
            return "Request must be a JSON string"
        
        data = request.get_json()

        workflow = data.get("workflow")
        flowid = data.get("flowid")
        authToken = request.headers.get('Authorization')
        # authToken includes 'Bearer'

        # TODO: Move the logic to service and handler class...

        if workflow is None:
            return "Request must include value for 'workflow'"
        if flowid is None:
            return "Request must include value for 'flowid'"
        
        workflowOutputFile= flowid+'.cwl'
        
        stepList = []

        print("Reading models")
        for step, modelsSetList in workflow.items():
            print("Step -> "+step)
            for modelIndex, model in enumerate(modelsSetList):
                bodyData = ''
                prerequisitesList = []
                commandLineInputList = []
                print("Model -> "+str(modelIndex))
                print("Number of prerequisites: "+str(len(model.get("prerequisites"))))
                for prerequisite in model.get("prerequisites"):
                    prerequisiteId = prerequisite+"input"
                    prerequisitesList.append(cwl.WorkflowStepInput(
                        id=prerequisiteId,
                        source="Step"+prerequisite+"/"+prerequisite+"output"
                    ))
                    commandLineInputList.append(cwl.CommandInputParameter(
                        id=prerequisiteId,
                        type="File"
                    ))
                if("_transformation" not in model.get("id")): #describe model
                    bodyData = '@$(inputs.'+model.get('id')+'_transformationinput.path)'
                    stepList.append(cwl.WorkflowStep(
                        prerequisitesList,#inputs
                        [
                            cwl.WorkflowStepOutput(
                                id=model.get("id")+"output"
                            )
                        ],#outputs
                        run=cwl.CommandLineTool(
                            cwlVersion="v1.2",
                            baseCommand=["curl"],
                            inputs=commandLineInputList, #inputs
                            outputs=[
                                cwl.CommandOutputParameter(
                                    id=model.get("id")+"output",
                                    type="File",
                                    outputBinding=
                                        cwl.CommandOutputBinding(
                                            glob= model.get("id")+"output"
                                        )
                                )
                            ],
                            arguments=[
                                "-X", model.get("computationInfo").get("method"),
                                model.get("computationInfo").get("url"),
                                "-H", CONTENTTYPE + model.get("computationInfo").get("contentType"),
                                "-H", AUTH + authToken,
                                "--data-binary", bodyData #payload is contained in a file
                                
                            ],
                            stdout=model.get("id")+"output"
                        ),
                        id="Step" + model.get("id")
                    ))
                else: #transformation service (i.e. assembler)
                    # Prepare assembler payload
                    modelid=model.get("id").replace('_transformation','')
                    modelPrerequisitesIdList = []
                    for prerequisite in model.get("prerequisites"):
                        modelPrerequisitesIdList.append(prerequisite)
                    bodyData = {'flow_id': flowid, 'n_model_id': modelid, 'm_dependency_ids': modelPrerequisitesIdList}
                    bodyData = json.dumps(bodyData)
                    # Create a workflow step
                    stepList.append(cwl.WorkflowStep(
                        prerequisitesList,#inputs
                        [
                            cwl.WorkflowStepOutput(
                                id=model.get("id")+"output"
                            )
                        ],#outputs
                        run=cwl.CommandLineTool(
                            cwlVersion="v1.2",
                            baseCommand=["curl"],
                            inputs=commandLineInputList, #inputs
                            outputs=[
                                cwl.CommandOutputParameter(
                                    id=model.get("id")+"output",
                                    type="File",
                                    outputBinding=
                                        cwl.CommandOutputBinding(
                                            glob= model.get("id")+"output"
                                        )
                                )
                            ],
                            arguments=[
                                "-X", model.get("computationInfo").get("method"),
                                model.get("computationInfo").get("url"),
                                "-H", CONTENTTYPE + model.get("computationInfo").get("contentType"),
                                "-H", AUTH + authToken,
                                "-d", bodyData # Payload will be sent as plain text in the body
                            ],
                            stdout=model.get("id")+"output"
                        ),
                        id="Step" + model.get("id")
                    ))
        print("Reading models [Done]")
        
        print("Defining workflow")
        workflowCWL = cwl.Workflow(
            cwlVersion="v1.2",
            inputs=[
            ],
            outputs=[
                # cwl.WorkflowOutputParameter(
                #     type="File",
                #     id="output1",
                #     outputSource="StepM1/M1output" #hardcoded workflow output
                # )
            ],
            steps=stepList
        )
        print("Defining workflow [Done]")

        dict_representation = workflowCWL.save()
        yaml = YAML()

        print("Saving to file")
        with open(workflowOutputFile, 'w') as outfile:
            yaml.dump(dict_representation, outfile)
        print("Saving to file [Done:"+workflowOutputFile+"]")
        if not os.path.exists(workflowOutputFile):
            return json.dumps({'message':'Error creating CWL'})
        size = os.path.getsize(workflowOutputFile)
        print("Bytes written to file: "+str(size))

        return json.dumps({'message':'Success'})