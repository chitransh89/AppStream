from stream_consumer.kafka_consumer import KafkaConsumer
from stream_consumer.gpubsub_consumer import GPubSubConsumer


def factory(stream_mechanism):
    consumers = {
        "kafka": KafkaConsumer,
        "gpubsub": GPubSubConsumer
    }

    return consumers[stream_mechanism]()
