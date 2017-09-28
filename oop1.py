#!/usr/bin/env python


def main():
    # example_1()
    # example_2()
    # example_3()
    example_4()


class Thing(object):
    foo = "this is a string member"
    bar = 123  # this is a number member

    def __init__(self, fooval):
        self.foo = fooval

    def do_a_thing(self):
        print("did the thing")



def example_4():
    t = Thing("the foo")
    t.do_a_thing()


def example_3():
    t = Thing("foo from the constructor")
    print(t.foo)
    t_also = Thing("woooo")
    print(t_also.foo)


def example_2():
    t1 = Thing()
    t2 = Thing()

    t1.foo = "this is t1's foo"
    t2.foo = "this is t2's foo"

    print(t1.foo)
    print(t2.foo)


def example_1():
    t = Thing()
    string_var = "asdf"
    number_var = 1

    print(type(string_var))
    print(type(number_var))
    print(type(t))

    print(t.foo)
    print(t.bar)
    t.foo = "Hah!  I changed it!"
    print(t.foo)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
