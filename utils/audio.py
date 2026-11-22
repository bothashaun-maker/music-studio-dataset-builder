import numpy as np
import soundfile as sf
from pathlib import Path

def get_audio_info(path):
    info = sf.info(path)
    return {
        "sample_rate": info.samplerate,
        "frames": info.frames,
        "channels": info.channels,
        "duration": info.duration
    }

def convert_to_wav(input_path, output_path, target_sr=44100):
    # Using ffmpeg via subprocess if needed, but soundfile can do a lot
    data, sr = sf.read(input_path, always_2d=True)
    if sr != target_sr:
        # Simple resample, in production use resample_poly
        pass
    sf.write(output_path, data, target_sr)
