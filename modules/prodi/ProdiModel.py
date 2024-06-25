from core.CoreModel import CoreModel

class DosenModel(CoreModel):
    def __init__(self):
        super().__init__()
        self.table_name = "prodi"
        self.table_id = "id_prodi"
