from flask import Flask

# Membuat aplikasi Flask
app = Flask(__name__)


# Menentukan halaman utama (halaman depan)
@app.route("/")
def halo_dunia():
  return "Halo! Ini adalah website pertama saya pakai Python dan Flask!"


# Menjalankan server lokal
if __name__ == "__main__":
  app.run(debug=True)