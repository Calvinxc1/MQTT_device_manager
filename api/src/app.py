from flask import Flask
import logging

from .init_spec import init_spec
from .logging import init_root_logger
from .resources import init_resources

app = Flask(__name__)
logger = init_root_logger()

spec_path = './spec/_root.yml'
spec = init_spec(spec_path)

kwargs = {
    'spec': spec,
    #'validate_output': True,
    ## Set to bypass problem as outlined at https://github.com/p1c2u/openapi-core/issues/277.
}

api = init_resources(app, kwargs=kwargs)
