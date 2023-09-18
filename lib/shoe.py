#!/usr/bin/env python3

class Shoe:
    pass
    def __init__(self,brand, size): 
        self.brand = brand
        self.size = size

    def set_size(self, size):
        if type(size) != int: 
            print('size must be an integer')
        else:
            self._size = size
    def get_size(self):
        return self._size
    size = property(get_size, set_size)

    def cobble(self):
        print('Your shoe is as good as new!')

    condition = 'New'  
        