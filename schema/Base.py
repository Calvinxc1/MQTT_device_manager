import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
import typing

RootBase = declarative_base()

class Base(RootBase):
    
    ## Borrowed from https://stackoverflow.com/questions/24959589/get-table-columns-from-sqlalchemy-table-model
    def _as_dict(self):
        """
        Helper function that allows traversing the table's instance columns as key values

        :return: (key, value) iterator
        """
        for key in self.__table__.columns.keys():
            value = self.__getattribute__(key)
            yield key, value

    def __repr__(self):
        """
        General __repr__ implementation for an sqlalchemy table
        """
        values = []
        for key, value in self._as_dict():
            key_value_str = f"{key}={value}"
            values.append(key_value_str)

        values_str = ", ".join(values)
        cls_name = self.__class__.__name__
        return f"<{cls_name}({values_str})>"
