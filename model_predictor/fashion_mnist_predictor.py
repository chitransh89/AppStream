from tensorflow import keras
from utils import predictor
import numpy as np


class FashionMNISTModel(predictor.Predictor):

    def __init__(self, model_path):
        self.model = self.load_model(model_path)
        self.label_mapping = {0: "T-shirt/top", 1: "Trouser", 2: "Pullover", 3: "Dress", 4: "Coat",
                              5: "Sandal", 6: "Shirt", 7: "Sneaker", 8: "Bag", 9: "Ankle boot"}

    def load_model(self, model_path):
        return keras.models.load_model(model_path)

    def predict(self, img):
        """
        Predicts the scores for each level and returns the label with highest probability
        :param img:
        :return: Output class
        """
        return self.label_mapping[np.argmax(self.model.predict(img))]
