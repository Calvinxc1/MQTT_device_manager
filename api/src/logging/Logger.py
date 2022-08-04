from flask import request
from logging import LoggerAdapter, getLogger
from typing import Union

class Logger:
    """Class wrapper to provide consistent logging functionality through an application"""
    
    def _init_logging(self, endpoint:bool=False):
        """
        PARAMETERS
        -------
        endpoint - Should be set to `True` if being added to a Flask endpoint class
        """
            
        adapter = {'task': self.__class__.__name__ ,
                   'httpMethod': request.method if endpoint else '-',
                   'httpPath': request.url.split('?')[0] if endpoint else '-'}
        
        self._logger = LoggerAdapter(getLogger(self.__module__), adapter)
