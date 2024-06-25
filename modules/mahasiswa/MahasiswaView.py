from flask import *
from modules.dashboard.DashboardModel import *
from modules.mahasiswa.MahasiswaModel import *
from modules.prodi.ProdiModel import *

class MahasiswaView:
    
    @staticmethod
    def index():
        return render_template('mahasiswa_index.html')

    # sub menu tabel data mahasiswa
    @staticmethod
    def tabelmahasiswa():
        data_mahasiswa = MahasiswaModel().all_mahasiswa()
        return render_template('mahasiswa_tabelmahasiswa.html', data_mahasiswa = data_mahasiswa)

    # sub menu informasi mahasiswa
    @staticmethod
    def informasi():
        return render_template('mahasiswa_informasi.html')

    @staticmethod
    def create():
        data_prodi = ProdiModel().get_all_prodi()
        return render_template('mahasiswa_create.html', data_prodi = data_prodi)

    @staticmethod
    def edit(id):
        obj = MahasiswaModel().find(id)
        data_prodi = ProdiModel().get_all_prodi()
        return render_template('mahasiswa_edit.html', obj = obj, data_prodi = data_prodi)

    @staticmethod
    def store():
        obj = MahasiswaModel()
        post = request.form
        nim = post['nim']

        # Check if nim already exists in the database
        if MahasiswaModel().find_by_nim(nim):
            pesan_alert = 'NIM ini sudah ada. Harap cek kembali !'
            flash(pesan_alert, 'warning')
            return redirect(url_for('app_mahasiswa.index'))
        
        obj.nim = nim
        obj.nama = post['nama']
        id_prodi = post['id_prodi']

        # jika select option prodi belum dipilih
        if not id_prodi:
            pesan_id_prodi = 'Silahkan pilih Prodi !'
            flash(pesan_id_prodi,'warning')
            return redirect(url_for('app_mahasiswa.create'))
        
        obj.id_prodi = id_prodi

        MahasiswaModel.store(obj,obj)

        pesan_alert = 'Data berhasil disimpan !'
        flash(pesan_alert, 'success')
        return redirect(url_for('app_mahasiswa.index'))

    @staticmethod
    def update(id):
        data = MahasiswaModel().find(id)
        if data:
            post = request.form
            mahasiswa_obj = MahasiswaModel()

            mahasiswa_obj.nim = post['nim']
            mahasiswa_obj.nama = post['nama']
            mahasiswa_obj.id_prodi = post['id_prodi']

            MahasiswaModel().update(id, mahasiswa_obj)

            pesan_alert = 'Data berhasil diubah !'
            flash(pesan_alert, 'success')
            return redirect(url_for('app_mahasiswa.index'))
        else:
            return redirect(request.referrer)

    @staticmethod
    def delete(id):
        data = MahasiswaModel().find(id)
        if data:
            MahasiswaModel().delete(id)
            pesan_alert = 'Data berhasil dihapus !'
            flash(pesan_alert, 'success')
            return redirect(url_for('app_mahasiswa.index'))
        else:
            return redirect(request.referrer)

