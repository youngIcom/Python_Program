import unittest

class TestStringMethods(unittest.TestCase):
    #ini adalah test case pertama
    def test_strip(self):
        self.assertEqual('www.freelancer.com'.strip('c.mow'), 'freelancer')

    #ini test kedua
    def test_isalnum(self):
        self.assertTrue('c0d1ng'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())

    #ini test ketiga
    def test_index(self):
        s = 'dicoding'

        self.assertEqual(s.index('coding'), 2)

        #cek s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index('decode')


if __name__ == '__main__':
    #test runner
    unittest.main()
