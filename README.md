# Workflow CWL Wrapper
Web service wrapper for the Common Workflow Language API. 
The service provides two endpoints:
    - serialize: Converts a workflow plan in JSON format to CWL.
    - run: Executes a CWL workflow plan with a pre-assigned flow identifier.

This microservice forms part of the SWIM model orchestration pool, for more information view:   
https://water.cybershare.utep.edu/resources/docs/en2/backend/swim-broker/


## Build and Run

### Option 1: Pull Docker Image   
Environment Requirements: Docker and Docker Compose

The public image of the Workflow Composer can be pulled from the Dockerhub repo:  
lagarnicachavira/workflow-cwl-public   
https://hub.docker.com/r/lagarnicachavira/workflow-cwl-public   

You can directly run the application using the docker-compose.yml in this repo.

1) Modify the file docker-compose.yml if necesary.
2) Run the container: > docker-compose up (linux)  |  docker compose up (windows)
3) Once running, the OpenAPI documentation will be locally available at http://localhost:5004/workflow-cwl/docs/

### Option 2: Build Docker Container   
Environment Requirements: Docker

The Workflow Composer can be deployed as a docker container using Docker Build or Compose.

1) Download this repository into a folder on your machine.
2) Install Docker and Docker composer on your target machine.
3) Setup your docker account at: https://www.docker.com/get-started
4) Using a command line or terminal navigate to the base path of the project.
5) Build the image: > docker build -t workflow-cwl-public:latest.
6) Run the container: > docker run -p 5004:5004 workflow-cwl-public:latest .
7) Once running, the API documentation will be locally available at http://localhost:5004/workflow-cwl/docs/

### Option 3: Build and Run Natively   
Environment Requirements: Python 3+, pip, python virtual env  

    - Install Python > 3
    - Setup a python virtual environment and activate  
    - Comment the uWSGI package on requirements.txt if running on windows
    - pip install -r requirements.txt

CLI Run Commands:
    localhost run server (development mode): > py manage.py run (windows)   
    API documentation will be locally available at http://localhost:5004/workflow-cwl/docs/   

## Testing
The tests folder in this repository contains input and output files used as an abstract test case
and the SWIM (http://purl.org/swim) case study. 

You may use the abstract sample files for quick demo purposes, the abstract input can be serialized, but not executed.
The generated serialization is saved in the root of the container, the response is just an acknowledgement of the serialization process.

## OpenAPI Screenshots

### OpenAPI Documentation Screenshot
![Endpoints](/images/endpoints.png "Endpoint screenshot")

### Abstract Example Input
![Serializer Input](/images/abstract_serialize_input.png "Abstract Example Input")

### Abstract Example Input
![Serializer Output](/images/abstract_serialize_output.png "Abstract Example Output")

## Contributors
Raul Alejandro Vargas Acosta   
Luis Garnica Chavira   
Natalia Villanueva-Rosales   
Deana D. Pennington     

## Acknowledgements
This material is based upon work supported by the National Science Foundation (NSF) under Grant No. 1835897. This work used resources from Cyber-ShARE Center of Excellence, which is supported by NSF Grant number HRD-1242122.
Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the NSF.

## License
GNU GENERAL PUBLIC LICENSE v3.0

## Copyright
© 2022 - University of Texas at El Paso (SWIM Project).

## References
[1] P. Amstutz et al., “Common Workflow Language, v1.0,” 2016, doi: https://doi.org/10.6084/m9.figshare.3115156.v2.







