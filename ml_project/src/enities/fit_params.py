from dataclasses import dataclass
from marshmallow_dataclass import class_schema
import yaml


@dataclass()
class FitParams:
    x_train_path: str
    y_train_path: str
    output_model_path: str
    model_type: str


FitParamsSchema = class_schema(FitParams)


def read_fit_params(path: str) -> FitParams:
    with open(path, "r") as fin:
        schema = FitParamsSchema()
        return schema.load(yaml.safe_load(fin))
