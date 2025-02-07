
import os

def create_python_files(num_files=100, prefix="Exercise_"):
    for i in range(12, num_files + 1):
        filename = f"{prefix}{i}.py"
        with open(filename, "w"):
            pass


if __name__ == "__main__":
    create_python_files()
