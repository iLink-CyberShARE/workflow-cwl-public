# Workflow CWL Wrapper
Web service wrapper for the Common Workflow Language API. 
The service provides two endpoints:
    - serialize: 
    - run: 

## OpenAPI Docs path
http://localhost:5004/workflow-cwl/docs/

## OpenAPI Screenshots


## Docker Container

The Workflow CWL Wrapper can be deployed as a docker container.
Docker Build and Compose

1) Download this repository into a folder on your machine.
2) Install Docker and Docker composer on your target machine.
3) Setup your docker account at: https://www.docker.com/get-started
4) Using a command line or terminal navigate to the base path of the project.
5) Build the image: > docker build -t workflow-cwl-public:latest.
6) Modify the file docker-compose.yml if necesary.
6) Run the container: > docker-compose up
7) Once running, the API documentation will be locally available at http://localhost:5004/workflow-cwl/docs/


The public image of the CWL-wrapper can also be pulled from dockerhub repo: lagarnicachavira/workflow-cwl-public

## Native Installation
    - Install Python > 3
    - Setup a python virtual environment and activate  
    - Comment the uWSGI package on requirements.txt if running on windows
    - pip install -r requirements.txt

### CLI Run Commands:
    localhost run server (development mode): > py manage.py run (windows)   
    API documentation will be locally available at http://localhost:5004/workflow-cwl/docs/

## Acknowledgements
This material is based upon work supported by the National Science Foundation (NSF) under Grant No. 1835897. This work used resources from Cyber-ShARE Center of Excellence, which is supported by NSF Grant number HRD-1242122.
Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the NSF.

## Contributors
Project PI - Natalia Villanueva-Rosales
Project Co-PI - Deana D. Pennington
Project Co-PI - Josiah Heyman
Developer - Raul Alejandro Vargas Acosta
Developer - Luis Garnica Chavira

## License
GNU GENERAL PUBLIC LICENSE v3.0

## Copyright
© 2022 - University of Texas at El Paso (SWIM Project).

## References
[1] P. Amstutz et al., “Common Workflow Language, v1.0,” 2016, doi: https://doi.org/10.6084/m9.figshare.3115156.v2.







