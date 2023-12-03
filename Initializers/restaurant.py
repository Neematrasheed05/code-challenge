#Restaurant __init__()`
#Restaurants should be initialized with a name, as a string
#Restaurant name()`
#returns the restaurant's name
# should not be able to change after the restaurant is created

from typing import Any


class Restaurant:
    def __init__(self, name):
        self._name = name
    
    def __setattr__(self, name: str, value: Any) -> None:
        if name == "_name" and hasattr(self, "_name"):
            print("Attribute '_name' cannot be changed after the restaurant is created.")
        else:
            super().__setattr__(name, value)

    def name(self):
        return self._name

