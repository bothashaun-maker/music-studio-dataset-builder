# Music Studio Dataset Builder

Builds music datasets by separating songs into stems with RoFormer models,
saving each run to an organized job folder with metadata and a ZIP of the stems.

## Features

- **Multi-Model Stem Separation**: 2-, 4- and 6-stem separation with the
  RoFormer models listed below
- **Dataset Management**: organized output with metadata tracking and ZIP export
- **Quality Profiles**: overlap presets (`Balanced`, `Quality`,
  `Maximum overlap (slower)`) for different use cases
- **Metadata Tracking**: every run writes `result.json` with the run parameters,
  timings and device, plus checksums for each stem
- **Verified Models**: weights download from HuggingFace and pass SHA256 and
  size checks before use
- **Re-run Reuse**: a completed job with identical inputs and settings returns
  its saved stems without GPU work

## Architecture

### Core Components

1. **stem_studio/engine.py** - main processing engine with audio handling and
   model inference
2. **stem_studio/catalog.json** - model configurations and metadata
3. **stem_studio/assets.py** - model download and verification
4. **dataset_builder.py** - the `StemStudio` class that wraps model setup and
   separation runs
5. **utils/audio.py** - audio processing utilities
6. **utils/validation.py** - input validation and quality checks

### Supported Models

- **BS-RoFormer SW**: 6-stem separation (bass, drums, other, vocals, guitar, piano)
- **Kim Mel-Band RoFormer**: 2-stem separation (vocals/instrumental)
- **Viperx BS-RoFormer 12.9755**: alternative 2-stem separation

## Quick Start

```python
from dataset_builder import StemStudio

# Initialize with models directory (downloads and verifies weights on first use)
studio = StemStudio(models_dir="./models")

# Process a single track
result = studio.separate(
    input_path="song.wav",
    model="sw6",  # 6-stem
    mode="Six stems",
    profile="Balanced"
)

# Each job folder holds the stems, result.json and all_stems.zip
print(result["zip_path"])
```

Outputs land in `<models_dir>/../output/jobs/<id>/`. Note that
`export_dataset()` is a placeholder in this build — the run itself writes the
ZIP and `result.json`, so no extra export step is required.

## Improvements Over Original

- explicit error handling and validation checks (weight size/hash verification,
  disk-space checks, non-finite sample rejection)
- progress reporting through `progress.json` during a run
- per-run metadata in `result.json` (parameters, timings, device, peak VRAM)
- completed-job reuse: saved stems are returned when nothing about the source,
  model or settings has changed

## Requirements

- Python 3.8+
- PyTorch with CUDA support (recommended)
- bs-roformer==0.4.0
- soundfile
- numpy
- scipy

## Model Downloads

Models are downloaded automatically from HuggingFace and verified with SHA256
checksums and expected file sizes. Total size: about 2.1 GiB (2.25 GB) across
the three checkpoints.

## License

Original model licenses apply. This tool is for educational and research purposes.