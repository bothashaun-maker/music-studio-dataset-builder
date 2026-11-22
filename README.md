# Music Studio Dataset Builder

A comprehensive tool for building high-quality music datasets using advanced AI stem separation. Built on the proven RoFormer architecture with improvements for dataset creation and management.

## Features

- **Multi-Model Stem Separation**: Support for 2, 4, and 6-stem separation using state-of-the-art RoFormer models
- **Dataset Management**: Organized output with metadata tracking and ZIP export
- **Quality Profiles**: Balanced, Quality, and Maximum overlap settings for different use cases
- **ComfyUI Integration**: Optional workflow interface for visual processing pipeline
- **Batch Processing**: Process multiple tracks with consistent output formatting
- **Metadata Tracking**: Complete logging of processing parameters and results

## Architecture

### Core Components

1. **stem_studio/engine.py** - Main processing engine with audio handling and model inference
2. **stem_studio/catalog.json** - Model configurations and metadata
3. **stem_studio/workflows.json** - ComfyUI workflow definitions
4. **dataset_builder.py** - Dataset management and batch processing
5. **utils/audio.py** - Audio processing utilities
6. **utils/validation.py** - Input validation and quality checks

### Supported Models

- **BS-RoFormer SW**: 6-stem separation (bass, drums, other, vocals, guitar, piano)
- **Kim MelBandRoFormer**: 2-stem separation (vocals/instrumental)
- **Viperx BS-RoFormer**: Alternative 2-stem separation

## Quick Start

```python
from music_studio_dataset_builder import StemStudio

# Initialize with models directory
studio = StemStudio(models_dir="./models")

# Process a single track
result = studio.separate(
    input_path="song.wav",
    model="sw6",  # 6-stem
    mode="Six stems",
    profile="Balanced"
)

# Export dataset
studio.export_dataset(result, output_dir="./dataset")
```

## Improvements Over Original

- Enhanced error handling and validation
- Better memory management for long processing sessions
- Improved progress reporting
- Support for custom output naming
- Batch processing capabilities
- Dataset metadata tracking
- Cleaner code structure with type hints

## Requirements

- Python 3.8+
- PyTorch with CUDA support (recommended)
- bs-roformer==0.4.0
- soundfile
- numpy
- scipy

## Model Downloads

Models are automatically downloaded from HuggingFace and verified using SHA256 checksums. Total size: ~2.1GB.

## License

Original model licenses apply. This tool is for educational and research purposes.