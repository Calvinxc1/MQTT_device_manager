from ..Base import Base
from .delete import delete
from .get import get
from .put import put
from .post import post

class Device(Base):
    delete = delete
    get = get
    put = put
    post = post
