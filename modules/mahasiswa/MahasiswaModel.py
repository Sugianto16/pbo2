from core.CoreModel import CoreModel

class DosenModel(CoreModel):
    def __init__(self):
        super().__init__()
        self.table_name = "mahasiswa"
        self.table_id = "id_mahasiswa"
