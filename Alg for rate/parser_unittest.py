import unittest
import parser_for_train_data
import humor_checker_main
import sys

class LearningCase(unittest.TestCase):
    def test_starting_out(self):
        self.assertEqual(1, 1)

class TestCase(unittest.TestCase):
    
    def test_callCelebCorpus(self):
        self.assertEqual(humor_checker_main.callCelebCorpus("superman"), 0)

    def test_callMultiCorpus(self):
        self.assertEqual(humor_checker_main.callMultiCorpus("you feel"), 0)

    def test_callMainCorpus(self):
        self.assertEqual(humor_checker_main.callMainCorpus("feel"), 0)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass



def main():
    unittest.main()

if __name__ == "__main__":
    main()

def test_starting_out():
    assert 1 == 1

firstTestCase = TestCase('test_callCelebCorpus')
secondTestCase = TestCase('test_callMultiCorpus')
thirdTestCase = TestCase('test_callMainCorpus')

TestSuite = unittest.TestSuite()
TestSuite.addTest(TestCase('test_callCelebCorpus'))
TestSuite.addTest(TestCase('test_callMultiCorpus'))
TestSuite.addTest(TestCase('test_callMainCorpus'))