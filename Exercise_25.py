"""Define a class, which has a class parameter and has the same instance parameter.
Define an instance parameter, need add it in __init__ method
You can init an object with constructor parameter or set the value later"""


class MyClass:
    class_param = None

    def __init__(self, class_param=None):
        if class_param is not None:
            self.class_param = class_param


obj1 = MyClass("Hello")
print(obj1.class_param)

obj2 = MyClass()
print(obj2.class_param)
obj2.class_param="World"

print(obj2.class_param)
