import unittest
from my_file import MyClass


class ExampleTest(unittest.TestCase):
    def setUp(self):
        self.mc = MyClass()

    def test(self):
        self.assertTrue(True)

    def test2(self):
        self.assertFalse("")

    def test3(self):
        self.assertEqual(self.mc.m1(), 2)

    def test4(self):
        self.assertEqual(self.mc.m2(3), 9)


if __name__ == "__main__":
    unittest.main()
