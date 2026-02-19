import whisper

class WhisperSTT:
    def __init__(self, model_name="base"):
        print("🔄 Loading Whisper model...")
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path):
        result = self.model.transcribe(audio_path, fp16=False)
        return result["text"]
