import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan nama anda")
args = parser.parse_args()

print("Terimakasih telah menggunakan panggildicoding.py, "+args.nama)
