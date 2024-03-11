#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Handles storage of objects in JSON format."""

    __file_path = "file.json"
    __objects = {}
    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects
    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        dict_obj = {}
        for key, obj in FileStorage.__objects.items():
            dict_obj[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dict_obj, f)




