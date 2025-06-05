# htx-xdata-asr

## Task 2a Usage Instruction

- Open up _asr_api.py_ and ensure the pretrained model is to be loaded:

  ```
  # Uncomment the code below
  processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
  model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")

  # Comment the code below
  # processor = Wav2Vec2Processor.from_pretrained(
      "../asr-train/saved_models/wav2vec2-large-960h-cv")
  # model = Wav2Vec2ForCTC.from_pretrained(
      "../asr-train/saved_models/wav2vec2-large-960h-cv")
  ```

## Task 2b Usage Instruction

- Run the code below in one terminal:
  ```
  python asr_api.py
  ```
- Run the curl command below in another terminal:
  ```
  curl http://localhost:8001/ping
  ```
- Else, execute the API through an API platform such as Postman using:
  - URL: http://localhost:8001/ping

## Task 2c Usage Instruction

- Run the code below in one terminal:
  ```
  python asr_api.py
  ```
- Run the curl command below in another terminal:
  ```
  curl -F 'file=@/Users/gordon.oh/Desktop/htx-xdata-asr/asr/uploaded_files/sample-000000.mp3;type=audio/mpeg' http://localhost:8001/asr
  ```
- Else, execute the API through an API platform such as Postman using:
  - URL: http://localhost:8001/asr
  - Under _Body_ and _form-data_, add _file_ as the key of type file and upload the mp3 audio file as the value.

## Task 2d Usage Instruction

- Run the code below in one terminal:
  ```
  python asr_api.py
  ```
- Run the code below in another terminal (the script below will repeatedly call the /asr endpoint using all the files in _cv-valid-dev_):
  ```
  python cv-decode.py
  ```
- The file _cv-valid-dev-with-generated-text.csv_ will be generated, with all the transcription copied to the new column _generated_text_.

## Task 2e Usage Instruction

- Ensure that
  ```
  python asr_api.py
  ```
  ran from the previous task is stoppped.
- Build the Docker image from the Dockerfile using:
  ```
  docker build -t asr-api .
  ```
  - For machine with ZScaler configuration, the _ZscalerRootCertificate-2048-SHA256.crt_ must be placed in this directory. Then, build the Docker image from the Dockerfile using this command instead:
    ```
    docker build --build-arg INCLUDE_ZSCALER=true -t asr-api .
    ```
- Run the Docker image is build, run the Docker container using:
  ```
  docker run -p 8001:8001 --name asr-api asr-api
  ```
- To view and follow the logs of the running Docker container, use:
  ```
  docker logs -f asr-api
  ```
- Run the curl command below in another terminal:
  ```
  curl -F 'file=@/Users/gordon.oh/Desktop/htx-xdata-asr/asr/uploaded_files/sample-000000.mp3;type=audio/mpeg' http://localhost:8001/asr
  ```
- Else, execute the API through an API platform such as Postman using:
  - URL: http://localhost:8001/asr
  - Under _Body_ and _form-data_, add _file_ as the key of type file and upload the mp3 audio file as the value.
- To stop the Docker container, use:
  ```
  docker stop asr-api
  ```
- To remove the Docker image, use:
  ```
  docker rm asr-api
  ```

## Deliverables in this Directory

- _asr_api.py_ for Task 2a-c
- _cv-decode.py_ for Task 2d
- _cv-valid-dev-with-generated-text.csv_ for Task 2d
- _Dockerfile_ for Task 2e
