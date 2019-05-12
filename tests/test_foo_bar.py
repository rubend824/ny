import unittest
from ..foobar.classes.foobar import FooBar, Multiple


class TestMultiple(unittest.TestCase):
    def test_multiple_10(self):
        """Testes if 100 is multiple of 10"""
        self.assertEqual(Multiple.is_multiple(100, 10), True, 'Should be True')

    def test_multiple_5(self):
        """Testes if 43 is multiple of 5"""
        self.assertEqual(Multiple.is_multiple(43, 5), False, 'Should be False')


class TestFooBar(unittest.TestCase):

    def test_foobar_printable_value_bar(self):
        """Tests the printable value of 10. Should be bar"""
        foobar = FooBar(10)
        self.assertEqual(foobar.get_printable_value(), "Bar", "Should be Bar")

    def test_foobar_printable_value_number(self):
        """Tests the printable value of 43. Should be the number itself"""
        foobar = FooBar(43)
        self.assertEqual(foobar.get_printable_value(), "43", "Should be 43")

    def test_foobar_printable_value_foobar(self):
        """Tests the printable value of 30. Should be FooBar"""
        foobar = FooBar(30)
        self.assertEqual(foobar.get_printable_value(), "FooBar", "Should be FooBar")

    def test_foobar_printable_value_foo(self):
        """Tests the printable value of 66. Should be Foo"""
        foobar = FooBar(66)
        self.assertEqual(foobar.get_printable_value(), "Foo", "Should be Foo")


if __name__ == '__main__':
    unittest.main()
