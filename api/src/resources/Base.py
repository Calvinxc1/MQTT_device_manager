from datetime import datetime as dt
from flask import make_response, request
from flask_restful import Resource
import json as js
from openapi_core.validation.request.validators import RequestValidator
from openapi_core.validation.response.validators import ResponseValidator
from openapi_core.contrib.flask import FlaskOpenAPIRequest as Request, FlaskOpenAPIResponse as Response
from openapi_core.spec.paths import SpecPath as Spec
from pydantic import validate_arguments

from ..logging import Logger

class Base(Resource, Logger):
    @validate_arguments(config={'arbitrary_types_allowed':True})
    def __init__(self, spec:Spec, validate_output:bool=False):
        self._start_time = dt.now()
        self._init_logging(endpoint=True)
        self._spec = spec
        self._validate = validate_output
        
    def _get_request(self):
        self._logger.info('Received endpoint request')
        self._request = Request(request)
        validation = RequestValidator(self._spec).validate(self._request)
        
        errors = [str(error) for error in validation.errors]
        if errors:
            self._logger.warning(errors)
            data = None
        else:
            data = js.loads(self._request.body) \
                if self._request.body \
                else None
        
        return data, errors
    
    def _build_response(self, *args, **kwargs):
        resp = make_response(*args, **kwargs)
        if self._validate:
            validation = ResponseValidator(self._spec).validate(self._request, Response(resp))
            validation.raise_for_errors()
            
        self._logger.info(f'Request processed in {dt.now() - self._start_time}')
        return resp
