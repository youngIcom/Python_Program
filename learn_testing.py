import unittest

def koneksi_ke_db():
    print("[Terhubung ke db]")

def putus_koneksi_db(db):
    print("[koneksi terputus]")


class User:
    usename = ""
    aktif = False

    def __init__(self, username):
        self.username = username

    def set_aktif(self):
        self.aktif = True


class TestUser(unittest.TestCase):
    #test 1
    def test_user_default_not_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, "dicoding")
        self.assertFalse(dicoding.aktif)
        putus_koneksi_db(db)

    def test_user_default_active(self):
        db = koneksi_ke_db()
        dicoding = User(db, "dicoding")
        dicoding.set_aktif()
        self.assertTrue(dicoding.aktif)
        putus_koneksi_db(db)

if __name__ == "__main__":
    unittest.main()
