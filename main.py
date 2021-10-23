from utils.consumer_factory import factory


if __name__ == '__main__':
    consumer = factory('kafka')
    consumer.create_consumer(min_commit_count=5, host='localhost:9092')
    consumer.consume(["image-stream"])
