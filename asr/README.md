# htx-xdata-asr

## Usage Instruction (by Gordon Oh)

- Create a Python virtual environment for this project.
  ```
  python3 -m venv venv
  ```
- Activate the Python virtual environment.
  ```
  source venv/bin/activate
  ```
- Install required packages.
  ```
  pip install -r requirements.txt
  ```
- Start the backend.
  ```
  python manage.py run --port 8000 --reload
  ```

curl -F 'file=@/Users/gordon.oh/Desktop/htx-xdata-asr/asr/uploaded_files/sample-000000.mp3;type=audio/mpeg' http://localhost:8001/asr

docker build -t asr-api .
docker build --build-arg INCLUDE_ZSCALER=true -t asr-api .

docker run -p 8001:8001 --name asr-api asr-api

docker logs -f asr-api

docker stop asr-api
docker rm asr-api
