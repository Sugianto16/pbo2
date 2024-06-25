from core.CoreModel import CoreModel

class DashboardModel(CoreModel):
    def __init__(self):
        super().__init__()
        self.table_name = ""
        self.table_id = ""
