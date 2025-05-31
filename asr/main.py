from flask import Flask, request
from werkzeug.exceptions import HTTPException
from utils import *
from asr_api import (transcribe_audio, validate_mp3, get_sampling_rate,
                     REQUIRED_SAMPLING_RATE)

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    logger.info("Received ping request")
    return make_response(message="pong")


@app.route('/asr', methods=['POST'])
def asr():
    # Ensure the request contains a file
    if 'file' not in request.files:
        return make_response(code=400, message="Missing 'file' as an input")

    file = request.files['file']

    # Check if the type of the file is mp3
    if file.content_type not in ['audio/mpeg', 'audio/mp3', 'audio/mpeg3']:
        return make_response(code=400,
                             message="Invalid file type, only mp3 allowed")

    audio_bytes = file.read()

    # Verify if the file is a valid MP3 audio
    is_valid = validate_mp3(audio_bytes)
    if not is_valid:
        return make_response(code=400,
                             message="Uploaded file is not a valid MP3 audio")

    # Save mp3 file
    file_path = save_mp3_file(file)

    # Verify if the sampling rate of the MP3 file is correct (16 kHz)
    sampling_rate = get_sampling_rate(file_path)
    if sampling_rate is None:
        return make_response(
            code=400,
            message="Could not determine the sampling rate of the MP3 file")
    elif sampling_rate != REQUIRED_SAMPLING_RATE:
        logger.warning(
            f"MP3 sampling rate is {sampling_rate} Hz, but {REQUIRED_SAMPLING_RATE} Hz is required. Resampling will be performed."
        )

    # ASR Logic
    result = transcribe_audio(audio_bytes)

    logger.info(
        f"Processed audio file: {file.filename}\n\nTranscription: {result.get('transcription')}\n\nDuration: {result.get('duration')}s"
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
