import cv2
from confluent_kafka import Producer
import os

p = Producer({'bootstrap.servers': 'localhost:9092'})


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


for data in os.listdir("../test_images"):
    print(data)
    img = cv2.imread("../test_images/"+data, 0)
    # print(img.shape)
    encoded_image = img.tobytes()
    # decoded_image = np.reshape(np.frombuffer(encoded_image, dtype=np.uint8), (1, 28, 28, 1))
    # print(decoded_image.shape)
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)
    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    p.produce('image-stream', str({"filename": data, "image": encoded_image}).encode("utf-8"), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()
