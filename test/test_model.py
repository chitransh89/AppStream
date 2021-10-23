from model_predictor import fashion_mnist_predictor
import cv2
import numpy as np


pred = fashion_mnist_predictor.FashionMNISTModel("/home/chitransh/Documents/fashion_mnist_model")
img = cv2.imread("/home/chitransh/Documents/img1.jpeg", 0)
print(img.shape)
img = np.reshape(img, (1, 28, 28, 1))
print(pred.predict(img))
