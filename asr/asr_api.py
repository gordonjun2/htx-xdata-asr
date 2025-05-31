from utils import logger
import torchaudio
import torch

REQUIRED_SAMPLING_RATE = 16000


def transcribe_audio(waveform, sampling_rate, processor, model):

    # Resample if needed
    if sampling_rate != REQUIRED_SAMPLING_RATE:
        logger.warning(
            f"MP3 sampling rate is {sampling_rate} Hz, but {REQUIRED_SAMPLING_RATE} Hz is required. Resampling will be performed."
        )
        resampler = torchaudio.transforms.Resample(
            orig_freq=sampling_rate, new_freq=REQUIRED_SAMPLING_RATE)
        waveform = resampler(waveform)

    # Convert to mono (not required using common-voice dataset)
    if waveform.shape[0] > 1:
        waveform = waveform.mean(dim=0, keepdim=True)

    # Inference
    input_values = processor(waveform.squeeze().numpy(),
                             return_tensors="pt",
                             padding="longest",
                             sampling_rate=REQUIRED_SAMPLING_RATE).input_values

    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]

    duration = waveform.shape[1] / REQUIRED_SAMPLING_RATE

    return {"transcription": transcription, "duration": duration}
