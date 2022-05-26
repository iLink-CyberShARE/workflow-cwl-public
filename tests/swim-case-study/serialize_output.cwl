class: Workflow
inputs: []
outputs: []
cwlVersion: v1.2
steps:
- id: Step7b7ac93638f711ec8d3d0242_transformation
  in: []
  out:
  - id: 7b7ac93638f711ec8d3d0242_transformationoutput
  run:
    class: CommandLineTool
    inputs: []
    outputs:
    - id: 7b7ac93638f711ec8d3d0242_transformationoutput
      type: File
      outputBinding:
        glob: 7b7ac93638f711ec8d3d0242_transformationoutput
    cwlVersion: v1.2
    baseCommand:
    - curl
    arguments:
    - -X
    - POST
    - https://p1-endpoint-url.com/swim-assembler/assemble/
    - -H
    - 'Content-Type: application/json'
    - -H
    - 'Authorization: dummy-token'
    - -d
    - '{"flow_id": "test-id", "n_model_id": "7b7ac93638f711ec8d3d0242", "m_dependency_ids":
      []}'
    stdout: 7b7ac93638f711ec8d3d0242_transformationoutput
- id: Step7b7ac93638f711ec8d3d0242
  in:
  - id: 7b7ac93638f711ec8d3d0242_transformationinput
    source: Step7b7ac93638f711ec8d3d0242_transformation\7b7ac93638f711ec8d3d0242_transformationoutput
  out:
  - id: 7b7ac93638f711ec8d3d0242output
  run:
    class: CommandLineTool
    inputs:
    - id: 7b7ac93638f711ec8d3d0242_transformationinput
      type: File
    outputs:
    - id: 7b7ac93638f711ec8d3d0242output
      type: File
      outputBinding:
        glob: 7b7ac93638f711ec8d3d0242output
    cwlVersion: v1.2
    baseCommand:
    - curl
    arguments:
    - -X
    - POST
    - https://p2-endpoint-url.com/swim-wb-py/model/run
    - -H
    - 'Content-Type: application/json'
    - -H
    - 'Authorization: dummy-token'
    - --data-binary
    - '@$(inputs.7b7ac93638f711ec8d3d0242_transformationinput.path)'
    stdout: 7b7ac93638f711ec8d3d0242output
- id: Step5d8cdb841328534298eacf4a_transformation
  in:
  - id: 7b7ac93638f711ec8d3d0242input
    source: Step7b7ac93638f711ec8d3d0242\7b7ac93638f711ec8d3d0242output
  out:
  - id: 5d8cdb841328534298eacf4a_transformationoutput
  run:
    class: CommandLineTool
    inputs:
    - id: 7b7ac93638f711ec8d3d0242input
      type: File
    outputs:
    - id: 5d8cdb841328534298eacf4a_transformationoutput
      type: File
      outputBinding:
        glob: 5d8cdb841328534298eacf4a_transformationoutput
    cwlVersion: v1.2
    baseCommand:
    - curl
    arguments:
    - -X
    - POST
    - https://p3-endpoint-url.com/swim-assembler/assemble/
    - -H
    - 'Content-Type: application/json'
    - -H
    - 'Authorization: dummy-token'
    - -d
    - '{"flow_id": "test-id", "n_model_id": "5d8cdb841328534298eacf4a", "m_dependency_ids":
      ["7b7ac93638f711ec8d3d0242"]}'
    stdout: 5d8cdb841328534298eacf4a_transformationoutput
- id: Step5d8cdb841328534298eacf4a
  in:
  - id: 5d8cdb841328534298eacf4a_transformationinput
    source: Step5d8cdb841328534298eacf4a_transformation\5d8cdb841328534298eacf4a_transformationoutput
  - id: 7b7ac93638f711ec8d3d0242input
    source: Step7b7ac93638f711ec8d3d0242\7b7ac93638f711ec8d3d0242output
  out:
  - id: 5d8cdb841328534298eacf4aoutput
  run:
    class: CommandLineTool
    inputs:
    - id: 5d8cdb841328534298eacf4a_transformationinput
      type: File
    - id: 7b7ac93638f711ec8d3d0242input
      type: File
    outputs:
    - id: 5d8cdb841328534298eacf4aoutput
      type: File
      outputBinding:
        glob: 5d8cdb841328534298eacf4aoutput
    cwlVersion: v1.2
    baseCommand:
    - curl
    arguments:
    - -X
    - POST
    - https://p4-endpoint-url.com/user-scenario-input/
    - -H
    - 'Content-Type: application/json'
    - -H
    - 'Authorization: dummy-token'
    - --data-binary
    - '@$(inputs.5d8cdb841328534298eacf4a_transformationinput.path)'
    stdout: 5d8cdb841328534298eacf4aoutput
