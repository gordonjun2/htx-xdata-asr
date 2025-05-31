import requests
from huggingface_hub import configure_http_backend
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def backend_factory() -> requests.Session:
    session = requests.Session()
    session.verify = False
    return session


configure_http_backend(backend_factory=backend_factory)

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")
