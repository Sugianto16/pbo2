from abc import ABC, abstractmethod

class DashbordInterface(ABC):
    @abstractmethod
    def all():
        pass

    @abstractmethod
    def store(dashbord_obj):
        pass

    @abstractmethod
    def find(dashbord_id):
        pass

    @abstractmethod
    def update(dashbord_id, dashbord_obj):
        pass

    @abstractmethod
    def delete(dashbord_id):
        pass
