from utils import consumer
from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
# from configuration.config import GOOGLE_PROJECT_ID, PUB_SUB_SUBSCRIPTION_ID, PUB_SUB_TIMEOUT


class GPubSubConsumer(consumer.Consumer):

    def __init__(self):
        self.consumer = None
        self.timeout = None
        self.__project_id = None

    @staticmethod
    def callback(message: pubsub_v1.subscriber.message.Message):
        """
        Acknowledgement callback for message consumption
        :param message: Message Object
        :return: None
        """
        # print(f"Received {message}.")
        message.ack()

    def create_consumer(self, **kwargs):
        """
        Creates Consumer
        :param kwargs: google project id, pub sub subscription id
        :return: None
        """
        self.__project_id = kwargs.get("GOOGLE_PROJECT_ID", False)
        # self.__subs_id = kwargs.get("PUB_SUB_SUBSCRIPTION_ID", False)
        self.timeout = kwargs.get("timeout", 5)
        if self.__project_id and self.__subs_id:
            raise Exception("Project / Subscription Details missing")
        self.consumer = pubsub_v1.SubscriberClient()
        # The `subscription_path` method creates a fully qualified identifier
        # in the form `projects/{project_id}/subscriptions/{subscription_id}`

    def consume(self, topic):
        """
        Consumes message from the queue
        :param topic: List of topics
        :return:
        """
        subscription_path = self.consumer.subscription_path(self.__project_id, topic[0])
        streaming_pull_future = self.consumer.subscribe(subscription_path, callback=self.callback)
        with self.consumer:
            try:
                # When `timeout` is not set, result() will block indefinitely,
                # unless an exception is encountered first.
                streaming_pull_future.result(timeout=self.timeout)
            except TimeoutError:
                # Trigger the shutdown
                streaming_pull_future.cancel()
                # Block until the shutdown is complete.
                streaming_pull_future.result()
