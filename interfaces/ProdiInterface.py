from abc import ABC, abstractmethod

class ProdiInterface(ABC):
    @abstractmethod
    def all():
        pass

    @abstractmethod
    def store(prodi_obj):
        pass

    @abstractmethod
    def find(prodi_id):
        pass

    @abstractmethod
    def update(prodi_id, prodi_obj):
        pass

    @abstractmethod
    def delete(prodi_id):
        pass
