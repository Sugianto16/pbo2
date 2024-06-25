from flask import Flask, url_for, request, render_template
from modules.dashboard.DashboardRoute import app_dashboard
from modules.mahasiswa.MahasiswaRoute import app_mahasiswa
from modules.prodi.ProdiRoute import app_prodi

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Dibutuhkan untuk menggunakan flash

# registrasi blueprint untuk rute dashboard
app.register_blueprint(app_dashboard, url_prefix='/')

# registrasi blueprint untuk rute mahasiswa dibawah blueprint dosen
app.register_blueprint(app_mahasiswa, url_prefix='/mahasiswa')

# registrasi blueprint untuk rute prodi
app.register_blueprint(app_prodi, url_prefix='/prodi')

if __name__ == '__main__':
    app.run(debug=True)
