#!/usr/bin/env python

def main():
    c = Cat("CoolCat")
    d = Dog("Tank")

    animals = []
    animals.append(c)
    animals.append(d)

    for animal in animals:
        animal.speak()


class Animal(object):
    sound = "...silence"
    name = "Animal?"

    def speak(self):
        print(self.sound)


class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.sound = "woof"


class Cat(Animal):
    def __init__(self, name):
        self.name = name
        self.sound = "meow"


if __name__ == '__main__':
    main()
