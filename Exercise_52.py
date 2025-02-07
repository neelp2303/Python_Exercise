"""Define a class named American and its subclass NewYorker.
Use class Subclass(ParentClass) to define a subclass."""

class American:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def greet(self):
        print(f"Hello, my name is {self.name}. I'm an American.")

class NewYorker(American):
    def __init__(self, name, nationality, city):
        super().__init__(name, nationality)
        self.city = city
    
    def greet(self):
        print(f"Hello, my name is {self.name}. I'm a New Yorker from {self.city}.")
        super().greet()

# Example usage

american_person = American("John Doe", "American")
american_person.greet()

new_yorker_person = NewYorker("Jane Doe", "American", "New York")
new_yorker_person.greet()


