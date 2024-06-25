from flask import *
from modules.kelulusan.KelulusanView import *

app_kelulusan = Blueprint('app_kelulusan', __name__, template_folder='templates')

app_kelulusan.add_url_rule('/', 'index', MahasiswaView().index, methods=['GET'])

#class tombol tambah data
app_kelulusan.add_url_rule('/create', 'create', MahasiswaView().create, methods=['GET', 'POST'])

#class tombol edit
app_mahasiswa.add_url_rule('/edit/<int:id>', 'edit', MahasiswaView().edit, methods=['GET', 'POST'])

#class tombol simpan data
app_mahasiswa.add_url_rule('/store', 'store', MahasiswaView().store, methods=['POST'])

#class tombol update data
app_mahasiswa.add_url_rule('/update/<int:id>', 'update', MahasiswaView().update, methods=['POST'])

#class hapus data
app_mahasiswa.add_url_rule('/delete/<int:id>', 'delete', MahasiswaView().delete, methods=['GET', 'POST'])

