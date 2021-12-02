base_model.py#!/usr/bin/python

"""
BaseModel module
"""

import models
import uuid
from datetime import datetime


class BaseModel:
    
    """
    BaseModel class
    defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        
        """
        Init method
        """
        format_time = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, format_time)
                if k != "__class__":
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def __str__(self):
        """
        __str__: should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """

        di = dict(**self.__dict__)
        di['__class__'] = str(type(self).__name__)
        di['created_at'] = self.created_at.isoformat()
        di['updated_at'] = self.updated_at.isoformat()
        return (di)
