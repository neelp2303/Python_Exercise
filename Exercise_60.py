"""Define a custom exception class which takes a string message as an attribute.
To define a custom exception, we need to define a class inherited from Exception."""

class CustomException(Exception):
    def __init__(self, message):
        self.message = message

def main():
    try:
        # This will raise a custom exception
        raise CustomException("An error occurred")
    except CustomException as e:
        print(e.message)

if __name__ == "__main__":
    main()