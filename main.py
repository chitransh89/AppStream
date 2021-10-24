from utils.consumer_factory import factory
from configuration.config import KAFKA_HOST, KAFKA_TOPIC, KAFKA_MIN_COMMIT_COUNT, CONSUMER_TYPE

if __name__ == '__main__':
    consumer = factory(CONSUMER_TYPE)
    consumer.create_consumer(min_commit_count=KAFKA_MIN_COMMIT_COUNT, host=KAFKA_HOST)
    consumer.consume([KAFKA_TOPIC])
