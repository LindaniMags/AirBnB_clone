#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Defines the FileStorage class."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""

        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        
        s_objects = {obj: FileStorage.__objects[obj].to_dict() for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(s_objects, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects only if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                s_objects = json.load(f)
                for object in s_objects.values():
                    del object["__class__"]
                    self.new(eval(object["__class__"])(**object))
        except FileNotFoundError:
            return
