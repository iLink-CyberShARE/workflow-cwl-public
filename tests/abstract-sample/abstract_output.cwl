class: Workflow
inputs: []
outputs: []
cwlVersion: v1.2
steps:
- id: Stepp1
  in: []
  out:
  - id: p1output
  run:
    class: CommandLineTool
    inputs: []
    outputs:
    - id: p1output
      type: File
      outputBinding:
        glob: p1output
    cwlVersion: v1.2
    baseCommand:
    - curl
    arguments:
    - -X
    - POST
    - http://p1-endpoint-url.com
    - -H
    - 'Content-Type: Content-Type: application/json'
    - -H
    - 'Authorization: dummy-token'
    - --data-binary
    - '@$(inputs.p1_transformationinput.path)'
    stdout: p1output
- id: Stepp5
  in:
  - id: p1input
    source: Stepp1/p1output
  out:
  - id: p5output
  run:
    class: CommandLineTool
    inputs:
    - id: p1input
      type: File
    outputs:
    - id: p5output
      type: File
      outputBinding:
        glob: p5output
    cwlVersion: v1.2
    baseCommand:
    - curl
    arguments:
    - -X
    - POST
    - http://p5-endpoint-url.com
    - -H
    - 'Content-Type: Content-Type: application/json'
    - -H
    - 'Authorization: dummy-token'
    - --data-binary
    - '@$(inputs.p5_transformationinput.path)'
    stdout: p5output
- id: Stepp2
  in:
  - id: p1input
    source: Stepp1/p1output
  out:
  - id: p2output
  run:
    class: CommandLineTool
    inputs:
    - id: p1input
      type: File
    outputs:
    - id: p2output
      type: File
      outputBinding:
        glob: p2output
    cwlVersion: v1.2
    baseCommand:
    - curl
    arguments:
    - -X
    - POST
    - http://p2-endpoint-url.com
    - -H
    - 'Content-Type: Content-Type: application/json'
    - -H
    - 'Authorization: dummy-token'
    - --data-binary
    - '@$(inputs.p2_transformationinput.path)'
    stdout: p2output
- id: Stepp3
  in:
  - id: p1input
    source: Stepp1/p1output
  out:
  - id: p3output
  run:
    class: CommandLineTool
    inputs:
    - id: p1input
      type: File
    outputs:
    - id: p3output
      type: File
      outputBinding:
        glob: p3output
    cwlVersion: v1.2
    baseCommand:
    - curl
    arguments:
    - -X
    - POST
    - http://p3-endpoint-url.com
    - -H
    - 'Content-Type: Content-Type: application/json'
    - -H
    - 'Authorization: dummy-token'
    - --data-binary
    - '@$(inputs.p3_transformationinput.path)'
    stdout: p3output
- id: Stepp6
  in:
  - id: p1input
    source: Stepp1/p1output
  - id: p2input
    source: Stepp2/p2output
  - id: p3input
    source: Stepp3/p3output
  out:
  - id: p6output
  run:
    class: CommandLineTool
    inputs:
    - id: p1input
      type: File
    - id: p2input
      type: File
    - id: p3input
      type: File
    outputs:
    - id: p6output
      type: File
      outputBinding:
        glob: p6output
    cwlVersion: v1.2
    baseCommand:
    - curl
    arguments:
    - -X
    - POST
    - http://p6-endpoint-url.com
    - -H
    - 'Content-Type: Content-Type: application/json'
    - -H
    - 'Authorization: dummy-token'
    - --data-binary
    - '@$(inputs.p6_transformationinput.path)'
    stdout: p6output
