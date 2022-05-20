from flask import request
from flask_restplus import Resource
from ..util.dto import WFDto
import subprocess

api = WFDto.api2

@api.route('/')
class Execution(Resource):

    @api.doc('Runs a workflow serialized with CWL')
    @api.response(200, 'The request was received succesfully')
    @api.response(500, 'Internal error occured')
    @api.expect(WFDto.execModel)
    def put(self):
        """Runs a workflow serialized with CWL"""

        if not request.is_json:
            return "Request must be a JSON string"
        data = request.get_json()
        flowid = data.get("flowid")
        if flowid is None:
            return "Request must include value for 'flowid'"
        
        result = subprocess.run(['cwl-runner', flowid+".cwl"], stdout=subprocess.PIPE)

        return "You have the power!!!"
