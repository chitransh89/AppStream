from abc import ABC, abstractmethod


class Consumer(ABC):

    @staticmethod
    @abstractmethod
    def callback(*args):
        pass

    @abstractmethod
    def create_consumer(self, **kwargs):
        pass

    @abstractmethod
    def consume(self, topic):
        pass

    def close_connection(self):
        pass
