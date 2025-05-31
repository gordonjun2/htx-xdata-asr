from mutagen.mp3 import MP3
from mutagen import MutagenError
import ffmpeg
import io
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch
import torchaudio

REQUIRED_SAMPLING_RATE = 16000

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")


def validate_mp3(audio_bytes):
    try:
        audio = MP3(io.BytesIO(audio_bytes))
    except MutagenError:
        return False

    return True


def get_sampling_rate(audio_file):
    print(audio_file)
    try:
        probe = ffmpeg.probe(audio_file)
        for stream in probe['streams']:
            if stream['codec_type'] == 'audio':
                return int(stream.get('sample_rate'))
    except Exception as e:
        return None

    return None


def transcribe_audio(audio_bytes):

    transcription = "BEFORE HE HAD TIME TO ANSWER A MUCH ENCUMBERED VERA BURST INTO THE ROOM"

    duration = "20.7"

    # waveform, sample_rate = torchaudio.load(io.BytesIO(audio_bytes))

    # # Resample if needed
    # if sample_rate != REQUIRED_SAMPLING_RATE:
    #     resampler = torchaudio.transforms.Resample(
    #         orig_freq=sample_rate, new_freq=REQUIRED_SAMPLING_RATE)
    #     waveform = resampler(waveform)

    # # Convert to mono
    # if waveform.shape[0] > 1:
    #     waveform = waveform.mean(dim=0, keepdim=True)

    # input_values = processor(waveform.squeeze().numpy(),
    #                          return_tensors="pt",
    #                          sampling_rate=REQUIRED_SAMPLING_RATE).input_values

    # logits = model(input_values).logits
    # predicted_ids = torch.argmax(logits, dim=-1)
    # transcription = processor.batch_decode(predicted_ids)[0]

    # duration = waveform.shape[1] / REQUIRED_SAMPLING_RATE

    return {"transcription": transcription, "duration": duration}
