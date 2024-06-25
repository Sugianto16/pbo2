from flask import *
from modules.prodi.ProdiView import *

app_prodi = Blueprint('app_prodi', __name__, template_folder='templates')

app_prodi.add_url_rule('/', 'index', ProdiView().index, methods=['GET'])

#class tombol tambah data
app_prodi.add_url_rule('/create', 'create', ProdiView().create, methods=['GET', 'POST'])

#class tombol edit
app_prodi.add_url_rule('/edit/<int:id>', 'edit', ProdiView().edit, methods=['GET', 'POST'])

#class tombol simpan data
app_prodi.add_url_rule('/store', 'store', ProdiView().store, methods=['POST'])

#class tombol update data
app_prodi.add_url_rule('/update/<int:id>', 'update', ProdiView().update, methods=['POST'])

#class hapus data
app_prodi.add_url_rule('/delete/<int:id>', 'delete', ProdiView().delete, methods=['GET', 'POST'])

