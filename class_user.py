# Fix the code so that assertion does not throw any error

# Your code here


class User:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_name(self):
        return '{self.name} {self.surname}'.format(self=self)

    def get_age(self):
        return 'I am {self.age} years old'.format(self=self)


user = User('John', 'Doe', 23)
assert user.get_name() == 'John Doe'
assert user.get_age() == 'I am 23 years old'
