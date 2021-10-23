import numpy as np
import ast
import logging
from utils import consumer
from confluent_kafka import Consumer, KafkaError, KafkaException
from model_predictor.fashion_mnist_predictor import FashionMNISTModel



class KafkaConsumer(consumer.Consumer):

    def __init__(self, min_commit_count=10):
        self.consumer = None
        self.MIN_COMMIT_COUNT = None
        self.logger = logging.getLogger(__name__)
        self. model = FashionMNISTModel("model/fashion_mnist_model")

    @staticmethod
    def callback(err, partitions) -> None:
        """
        Acknowledgement callback for message consumption
        :param err: Error Object obtained while reading from broker
        :param partitions: Partition from which message is read
        :return:
        """
        if err:
            print(str(err))
        # else:
        #     print("Committed partition offsets: " + str(partitions))

    def create_consumer(self, **kwargs):
        """
        Creates Kafka Consumer
        :param kwargs: host and min_commit_count
        :return: None
        """
        self.MIN_COMMIT_COUNT = kwargs.get('min_commit_count')
        host = kwargs.get("host", None)
        if host is None:
            raise Exception("Host Key Missing")
        # SPECIFY HOST IN THE FORM OF "ip1:9092, ip2:9092"
        conf = {'bootstrap.servers': host,
                'group.id': "foo",
                'auto.offset.reset': 'smallest',
                'on_commit': self.callback}

        self.consumer = Consumer(conf)

    def consume(self, topic):
        """
        Consumes message from the queue
        :param topic: List of topics
        :return: None
        """
        try:
            self.consumer.subscribe(topic)

            msg_count = 0
            while True:
                msg = self.consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event
                        self.logger.error('%% %s [%d] reached end at offset %d\n' %
                                          (msg.topic(), msg.partition(), msg.offset()))
                    elif msg.error():
                        raise KafkaException(msg.error())
                else:
                    try:
                        data = msg.value().decode("utf-8")
                        data_dict = ast.literal_eval(data)
                        decoded_image = np.frombuffer((data_dict["image"]), dtype=np.uint8)
                        buffer_image = np.reshape(decoded_image, (1, 28, 28, 1))
                        print(self.model.predict(buffer_image), data_dict["filename"])
                        msg_count += 1
                        if msg_count % self.MIN_COMMIT_COUNT == 0:
                            self.consumer.commit(asynchronous=True)
                    except Exception as ex:
                        self.logger.error(ex)
                        continue

        finally:
            # Close down consumer to commit final offsets.
            self.consumer.close()
