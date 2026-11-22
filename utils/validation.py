from pathlib import Path

def validate_audio_file(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    # Additional validation logic (e.g., check duration, sample rate)
    return True

def validate_dataset_output(path):
    # Check if stems exist and are non-empty
    pass
