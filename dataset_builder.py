from pathlib import Path
import json
from .stem_studio.assets import build_pack
from .stem_studio.engine import run_job, CATALOG

class StemStudio:
    def __init__(self, models_dir="./models"):
        self.models_dir = Path(models_dir)
        self.models = build_pack(self.models_dir)
        self.catalog = CATALOG

    def separate(self, input_path, model="sw6", mode="Six stems", profile="Balanced"):
        # run_job returns result dictionary
        return run_job(
            source=input_path,
            model_key=model,
            mode=mode,
            profile=profile,
            models=self.models,
            output_root=self.models_dir.parent / "output"
        )

    def export_dataset(self, result, output_dir):
        # Placeholder for dataset export logic
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        # Further implementation based on requirements
        pass
