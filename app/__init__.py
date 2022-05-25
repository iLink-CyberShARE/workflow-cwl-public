from flask_restplus import Api
from flask import Blueprint, url_for

from .main.controller.workflow_serializer_controller import api as serializer_ns
from .main.controller.workflow_exec_controller import api as workflow_ns


blueprint = Blueprint('cwl', __name__, url_prefix='/workflow-cwl')

class CustomAPI(Api):
    @property
    def specs_url(self):
        '''
        The Swagger specifications absolute url (ie. `swagger.json`)
        This fix will force a relatve url to the specs.json instead of absolute
        :rtype: str
        '''
        return url_for(self.endpoint('specs'), _external=False)

authorizations = {
    'Bearer Auth' : {
        'type' : 'apiKey',
        'in' : 'header',
        'name' : 'Authorization',
        'description': 'Type in the value input box below: Bearer &lt;JWT&gt; where JWT is the token'
    }
}

api = CustomAPI(blueprint,
          title= "Workflow CWL",
          version='1.0',
          description='CWL serializer and wrapper webservice',
          doc='/docs/',
        #   security='Bearer Auth'
        #   authorizations = authorizations
          )

api.add_namespace(serializer_ns, path='/workflow/serialize')
api.add_namespace(workflow_ns, path='/workflow/execute')


