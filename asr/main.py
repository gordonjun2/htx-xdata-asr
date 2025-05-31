from flask import Flask, request
from werkzeug.exceptions import HTTPException
from utils import *
from asr_api import (transcribe_audio, REQUIRED_SAMPLING_RATE)
import torchaudio
import io
import requests
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from huggingface_hub import configure_http_backend
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)


def backend_factory() -> requests.Session:
    session = requests.Session()
    session.verify = False
    return session


configure_http_backend(backend_factory=backend_factory)

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")


@app.route('/ping', methods=['GET'])
def ping():
    logger.info("Received ping request")
    return make_response(message="pong")


@app.route('/asr', methods=['POST'])
def asr():
    # Ensure the request contains a file
    if 'file' not in request.files:
        return make_response(code=400, message="Missing 'file' as an input")

    # Only one file is allowed
    file = request.files['file']

    # Check if the type of the file is mp3
    if file.mimetype not in ['audio/mpeg', 'audio/mp3', 'audio/mpeg3']:
        return make_response(code=400,
                             message="Invalid file type, only mp3 allowed")

    audio_bytes = file.read()

    # Load the audio file using torchaudio
    try:
        waveform, sampling_rate = torchaudio.load(io.BytesIO(audio_bytes),
                                                  format="mp3")
    except:
        return make_response(code=400,
                             message="Uploaded file is not a valid MP3 audio")

    # # Save mp3 file after checking its validity
    # save_mp3_file(file)

    # ASR Logic
    result = transcribe_audio(waveform, sampling_rate, processor, model)

    logger.info(
        f"\nProcessed audio file: {file.filename}\n\nTranscription: {result.get('transcription')}\n\nDuration: {result.get('duration')}s"
    )

    return make_response(data=result)


@app.errorhandler(Exception)
def handle_all_exceptions(e):

    if isinstance(e, HTTPException):
        code = e.code
        message = e.description
    else:
        code = 500
        message = str(e)

    logger.exception("Unhandled Exception: %s", str(e))

    return make_response(code=code, message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
