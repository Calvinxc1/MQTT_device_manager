import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
import typing

RootBase = declarative_base()

class Base(RootBase):
    
    ## Borrowed from https://stackoverflow.com/questions/55713664/sqlalchemy-best-way-to-define-repr-for-large-tables
    def _repr(self, **fields: typing.Dict[str, typing.Any]) -> str:
        field_strings = []
        at_least_one_attached_attribute = False
        
        for key, field in fields.items():
            try:
                field_strings.append(f'{key}={field!r}')
            except sa.orm.exc.DetachedInstanceError:
                field_strings.append(f'{key}=DetachedInstanceError')
            else:
                at_least_one_attached_attribute = True
                
        if at_least_one_attached_attribute:
            return f"<{self.__class__.__name__}({','.join(field_strings)})>"
        
        return f"<{self.__class__.__name__} {id(self)}>"
