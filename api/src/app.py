from flask import Flask
import logging

from .init_spec import init_spec
from .logging import init_root_logger
from .resources import init_resources

app = Flask(__name__)
logger = init_root_logger(logging.INFO)

spec_path = './spec/_root.yml'
spec = init_spec(spec_path)

kwargs = {
    'spec': spec,
    
    ## Comment out to bypass potential problem as outlined
    ## at https://github.com/p1c2u/openapi-core/issues/277.
    'validate_output': True,
}

api = init_resources(app, kwargs=kwargs)
