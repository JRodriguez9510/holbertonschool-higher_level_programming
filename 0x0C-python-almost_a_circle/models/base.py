#!/usr/bin/python3
""" Module of a class base """
import json


class Base:
    """ A base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json representation of a list of dict """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of a list to a file """
        filename = cls.__name__ + ".json"
        lsto = []
        if lsto is not None:
            for i in list_objs:
                lsto.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(lsto))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        l = []
        try:
            with open(filename, 'r') as f:
                l = cls.from_json_string(f.read())
            for i, e in enumerate(l):
                l[i] = cls.create(**l[i])
        except:
            pass
        return l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ is "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        l = []
        try:
            with open(filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for args in csv_reader:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    l.append(obj)
        except:
            pass
        return l
