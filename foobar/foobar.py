"""
This is a program that prints all the numbers from 1 to 100.
However, for multiples of 3, instead of the number, it prints "Foo".
For multiples of 5. it prints "Bar". For numbers which are
multiples of both 3 and 5, it prints "FooBar"
"""

from classes.foobar import FooBar


if __name__ == '__main__':
    foobar = FooBar()
    for number in range(1, 101):
        foobar.set_number(number)
        printable_value = foobar.get_printable_value()
        print(printable_value)

