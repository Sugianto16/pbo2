from flask import *
from modules.dashboard.DashboardView import *

app_dashboard = Blueprint('app_dashboard', __name__, template_folder='templates')

app_dashboard.add_url_rule('/', 'index', DashboardView().index, methods=['GET'])

#class tombol tambah data
app_dashboard.add_url_rule('/create', 'create', DashboardView().create, methods=['GET', 'POST'])

#class tombol edit
app_dashboard.add_url_rule('/edit/<int:id>', 'edit', DashboardView().edit, methods=['GET', 'POST'])

#class tombol simpan data
app_dashboard.add_url_rule('/store', 'store', DashboardView().store, methods=['POST'])

#class tombol update data
app_dashboard.add_url_rule('/update/<int:id>', 'update', DashboardView().update, methods=['POST'])

#class hapus data
app_dashboard.add_url_rule('/delete/<int:id>', 'delete', DashboardView().delete, methods=['GET', 'POST'])

