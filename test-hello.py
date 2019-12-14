import unittest
import hello

class test_hello(unittest.TestCase):

    def test_duze(self):
        wynik = hello.duze('hello My world')
        self.assertEqual(wynik,'Hello my world')

    def test_fn(self):
        wynik = hello.fn('hello My world')
        self.assertEqual(wynik,6)

    def test_tyt(self):
        wynik = hello.tyt('hello My world')
        self.assertEqual(wynik,'Hello My World')

    def test_upp(self):
        wynik = hello.upp('hello My world')
        self.assertEqual(wynik,'HELLO MY WORLD')
    def test_swp(self):
        wynik = hello.swp('hello My world')
        self.assertEqual(wynik,'HELLO mY WORLD')
if __name__ == '__main__':
    unittest.main()
