from flask import Flask
from flask import request
from ruamel.yaml import YAML
import cwl_utils.parser_v1_2 as cwl
import json

app = Flask(__name__)

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

@app.route("/")
def main():
    print("Serializer: Start")
    workflowOutputFile='service.cwl'
    workflowInputDir = request.args.get('inputDir')
    workflowStr = request.args.get('workflow')
    authToken = request.args.get('auth')

    print("Check request")
    if(request is None or request.args is None or workflowInputDir is None
        or workflowStr is None or authToken is None):
        return "Bad sdfdsfdsfsdfrequest"
    print("Check request [Done]")

    workflowJSON = json.loads(workflowStr)
    workflowInputDir = "@"+workflowInputDir #curl command requires to add '@' for files

    stepList = []

    print("Reading models")
    for step, modelsSetList in workflowJSON.items():
        print("Step -> "+step)
        for modelIndex, model in enumerate(modelsSetList):
            prerequisitesList = []
            print("Model -> "+str(modelIndex))
            print("Prerequisites: ")
            if(model.get("prerequisites") is not None):
                print(len(model.get("prerequisites")))
                for prerequisite in model.get("prerequisites"):
                    prerequisitesList.append(cwl.WorkflowStepInput(
                        id=prerequisite+"input",
                        source="Step"+prerequisite+"/"+prerequisite+"output"
                    ))
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
                    inputs=[
                        
                    ],
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
                        "-H", model.get("computationInfo").get("contentType"),
                        "-H", "Authorization: Bearer "+ authToken,
                        "--data-binary", workflowInputDir
                    ],
                    stdout=model.get("id")+"output"
                ),#commands or workflows to execute
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
    print("Serializer finish")

    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)