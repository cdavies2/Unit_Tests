class Pet:
    def __init__(self, name, animal):
        if isinstance(name, str) == True & isinstance(animal, str) == True:
            self.name = name
            self.animal = animal
        else:
            raise (TypeError)


def firstItem(list1):
    return list1[0]


def cloneIt(x):
    y = x
    return y


def listFill(x, y):
    list1 = []
    for i in range(x, y + 1):
        list1.append(i)

    return list1


import unittest, os


class TestStringMethods(unittest.TestCase):

    # def test_index(self):
    #     list1=[0, 1, 2, 3, 4]
    #     self.assertEqual(0, list1[0])

    # def test_prime(self):
    #     x=5
    #     isPrime=True
    #     for i in range(2, x-1):
    #         if(x%i==0):
    #             isPrime=False
    #     self.assertTrue(isPrime==True)
    #     self.assertFalse(isPrime==False)

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)
    def test_first(self):
        list2 = [5, 6, 7, 8, 9]
        self.assertEqual(5, firstItem(list2))
        # make sure that firstItem fails when a nonlist or nonstring item is sent to it
        with self.assertRaises(TypeError):
            firstItem(45)

    def test_clone(self):
        x = 5
        y = cloneIt(x)
        self.assertIs(x, y)  # checks that x and y are the same object

    def test_fill(self):
        x = 3
        y = 10
        list1 = listFill(x, y)
        self.assertIn(x, list1)
        self.assertIn(y, list1)
        self.assertIn(
            y - x, list1
        )  # check that x, y, and 7 (a between value) are in the generated list
        self.assertNotIn(
            11, list1
        )  # check that a number out of range is not in the list

    def test_pets(self):
        pup = Pet("Sunny", "Dog")
        self.assertIsInstance(
            pup, Pet
        )  # make sure an object was created properly from the class
        with self.assertRaises(TypeError):
            fish = Pet(
                "Bubbles", 5
            )  # make sure the TypeError results if you send a nonString variable in

    # seeing if we can define a method inside of a unit test
    def test_method(self):
        dog = 5

        def hypo(dog: int):
            cat = dog + 1
            return cat

        cat = hypo(dog)
        self.assertTrue(cat > dog)

    # let's see if we can do unit tests that output and read in strings to text files
    def test_writing(self):
        current_dir = os.getcwd()
        file_dir = os.path.join(current_dir, "txt_files", "output.txt")

        def looper():
            tester = ""
            for i in range(0, 3):
                tester += "hello "
            with open(
                file_dir, "w", encoding="utf-8"
            ) as f:  # utf-8 is the encoding standard
                f.write(tester)  # this writes the tester string to the output.txt file

        looper()
        text_string = ""
        with open(file_dir, "r", encoding="utf-8") as f:
            text_string = (
                f.read()
            )  # this reads the string from output.txt and puts its value in text_string

        self.assertEqual(text_string, "hello hello hello ")


if __name__ == "__main__":
    unittest.main()

    # the number of tests ran is output, "OK" is output if there were no assert errors, all did what it should
