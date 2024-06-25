from abc import ABC, abstractmethod

class DashboardInterface(ABC):
    @abstractmethod
    def all():
        pass

    @abstractmethod
    def store(dashboard_obj):
        pass

    @abstractmethod
    def find(dashboard_id):
        pass

    @abstractmethod
    def update(dashboard_id, dashbord_obj):
        pass

    @abstractmethod
    def delete(dashboard_id):
        pass
