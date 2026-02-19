import numpy as np

class VAD:
    def __init__(self, sample_rate, threshold=0.01):
        self.threshold = threshold

    def is_speech(self, audio: np.ndarray) -> bool:
        energy = np.mean(audio ** 2)
        return energy > self.threshold
