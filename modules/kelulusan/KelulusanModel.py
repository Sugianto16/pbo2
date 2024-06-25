from core.CoreModel import CoreModel

class KelulusanModel(CoreModel):
    def __init__(self):
        super().__init__()
        self.table_name = "kelulusan"
        self.table_id = "id_kelulusan"
