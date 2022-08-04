from flask import Flask
from flask_restful import Api
from pydantic import validate_arguments

from .resource_map import resource_map

@validate_arguments(config={'arbitrary_types_allowed':True})
def init_resources(app:Flask, args:list=[], kwargs:dict={}) -> Api:
    api = Api(app)
    for resource, paths in resource_map.items():
        api.add_resource(resource, *paths,
                         resource_class_args=args,
                         resource_class_kwargs=kwargs)
        
    return api
