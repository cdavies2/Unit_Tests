import unittest

# Running Unit Tests Produced by the Models


# GPT-4
def add(a, b):
    return a + b


# create the simple addition function and test various conditions
class TestAddFunction(unittest.TestCase):
    def test_add_positives(self):
        self.assertEqual(add(1, 5), 6)

    def test_add_negatives(self):
        self.assertEqual(add(-5, -5), -10)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)


# All GPT-4 unittests execute properly


# Llama3
def add_numbers(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


def greet(name):
    return f"Hello, {name}"


class TestMathFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))

    def test_greet(self):
        self.assertEqual(greet("John"), "Hello, John")


class TestErrorHandling(unittest.TestCase):
    def test_add_numbers_error(self):
        with self.assertRaises(TypeError):
            add_numbers("a", 2)

    def test_is_even_error(self):
        with self.assertRaises(TypeError):
            is_even("a")

    @unittest.skip("debug")
    def test_greet_error(self):
        with self.assertRaises(TypeError):
            greet(123)

    # this particular test is skipped because, as written by Llama3, it doesn't work
    # because no type was specified for name, greet still runs even when an int is sent to it, no TypeError


if __name__ == "__main__":
    unittest.main()
