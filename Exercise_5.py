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