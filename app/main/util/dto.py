from flask_restplus import Namespace, fields

class WFDto:
    api = Namespace('/workflow/serialize', description='Serialize workflow')
    serializeModel = api.model('Serialize workflow', {
        'workflow': fields.String(required=True,
                           description="Workflow to serialize",
                           help="workflow cannot be blank.",
                           example="TBD"),
        'flowid': fields.String(required=True,
                           description="Flowid of the workflow to serialize",
                           help="flowid cannot be blank.",
                           example="TBD"),
    })

    api2 = Namespace('/workflow/execute', description="Execute workflow")
    execModel = api.model('Execute workflow', {
        'flowid': fields.String(required=True,
                           description="Flowid of the workflow to execute",
                           help="flowid cannot be blank.",
                           example="TBD"),
                           
    })

