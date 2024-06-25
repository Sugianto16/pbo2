from abc import ABC, abstractmethod

class KelulusanInterface(ABC):
    @abstractmethod
    def all():
        pass

    @abstractmethod
    def store(kelulusan_obj):
        pass

    @abstractmethod
    def find(kelulusan_id):
        pass

    @abstractmethod
    def update(kelulusan_id, kelulusan_obj):
        pass

    @abstractmethod
    def delete(kelulusan_id):
        pass
