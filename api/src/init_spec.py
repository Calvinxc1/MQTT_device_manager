from pathlib import Path
from openapi_core import create_spec
from openapi_core.spec.paths import SpecPath as Spec
from openapi_spec_validator.schemas import read_yaml_file
from pydantic import validate_arguments
import typing as t

@validate_arguments
def init_spec(spec_path:t.Union[str,Path]) -> Spec:
    if type(spec_path) is str:
        spec_path = Path(spec_path)
        
    spec_root = read_yaml_file(spec_path)
    spec_json = spec_parser(spec_root, spec_path.parents[0])
    spec = create_spec(spec_json)
    return spec

@validate_arguments
def spec_parser(yaml:t.Dict[str,t.Any], path:Path) -> t.Dict[str,t.Any]:
    if ('$ref' in yaml) and (not yaml['$ref'].startswith('#')):
        file = path / yaml['$ref']
        path = file.parents[0]
        yaml = read_yaml_file(file)
        
    new_yaml = {key: parser_items(val, path)
                for key, val in yaml.items()}
    return new_yaml

@validate_arguments
def parser_items(item:t.Any, path:Path) -> t.Any:
    if type(item) is dict:
        return spec_parser(item, path)
    
    elif type(item) is list:
        return [parser_items(sub_item, path)
                for sub_item in item]
    
    else:
        return item
