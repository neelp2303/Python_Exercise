"""Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include a simple test function to test the class methods.
Use __init__ method to construct some parameters"""


class Test:
    def __init__(self, string):
        self.string = string

    def getString(self):
        return self.string

    def printString(self):
        print(self.string)


def test():
    # Test Class instance
    string = input()
    obj = Test(string)

    # Printing string
    print("Testing get string method " + obj.getString())

    print("Testing printString method ")
    obj.printString()


test()
