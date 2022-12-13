#1. class Person name, fname, age, nationality; Constructor, print_info; instance
#2. class Student inherit Person + university, course: Constructor print_info; instance
#3. class Lecture inherit Person + university, experience
#4. class Check + method check(string) - check for open and close ()

class Person:
    def __init__(self, name, fname, age, nationality):
        self.name = name
        self.fname = fname
        self.age = age
        self.nationality = nationality

    def print_info(self):
        return f"My name is {self.name} {self.fname}. I am {self.age} tears old. My nationality is {self.nationality}."

class Student(Person):
    def __init__(self, person, university, course):
        super().__init__(person.name, person.fname, person.age, person.nationality)
        self.university = university
        self.course = course

    def print_info(self):
        return super().print_info() + f" I am student in {self.university} in {self.course}."

class Lecture(Person):
    def __init__(self, person, university, experience):
        super().__init__(person.name, person.fname, person.age, person.nationality)
        self.university = university
        self.experience = experience
    
    def print_info(self):
        return super().print_info() + f" I am lecture in {self.university} with {self.experience} years experience."

class Check:
    def check_brackets1(self, string):
        if len(string) % 2 == 1:
            return False
        brakets = ('()', '[]', '{}')
        while True in (b in string for b in brakets):
            for b in brakets:
                string = string.replace(b, '')
        return not string
    
    def check_brackets2(self, string):
        if len(string) % 2 == 1:
            return False
        brakets = ('(', ')', '[', ']', '{', '}')
        for open_bracket in brakets[::2]:
            while open_bracket in string:
                close_bracket = brakets[brakets.index(open_bracket)+1]
                if close_bracket in string[string.index(open_bracket)+1::]:
                    string = string.replace(open_bracket, '', 1)[::-1].replace(close_bracket, '', 1)[::-1]
                    print(string)
                else:
                    return False
        return not string


# p1 = Person("John", "Tolkien", 81, "Briton")
# print(p1.print_info())
# p2 = Person("Gregor", "Kolev", 19, "Bulgarian")
# print(p2.print_info())

# s1 = Student(p2, "TU", 1)
# print(s1.print_info())

# l1 = Lecture(p1, "TU", 20)
# print(l1.print_info())

print(Check().check_brackets2('({[]}[]())'))