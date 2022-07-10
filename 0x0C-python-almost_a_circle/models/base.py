#!/usr/bin/python3
"""
Class Base:
    private class attribute __nb_objects = 0
    class constructor: def __init__(self, id=None):
"""
import json


class Base:
    """created the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Update the class Base by adding the static method
        def to_json_string(list_dictionaries):
        that returns the JSON string representation of list_dictionaries:
        """
        if list_dictionaries is None:
            return "[]"
        else:
            string = json.dumps(list_dictionaries)
            return string

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes the JSON string
        representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        result = []
        if list_objs:
            for objs in list_objs:
                dictionary = objs.to_dictionary()
                result.append(dictionary)
        with open(filename, "w", encoding="UTF-8") as file:
            file.write(cls.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of the JSON
        string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Method that returns a list of instances"""
        filename = cls.__name__ + ".json"
        result = []
        try:
            with open(filename, encoding="utf-8") as file:
                obj_list = cls.from_json_string(file.read())
                for dictionary in obj_list:
                    result.append(cls.create(**dictionary))
                return result
        except Exception:
            return result
