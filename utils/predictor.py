from abc import ABC, abstractmethod


class Predictor(ABC):

    @abstractmethod
    def load_model(self, model_path):
        pass

    @abstractmethod
    def predict(self, img):
        pass
