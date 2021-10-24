import os

GOOGLE_PROJECT_ID = os.getenv("google_project_id", "")
PUB_SUB_SUBSCRIPTION_ID = os.getenv("google_pub_sub_id", "")
PUB_SUB_TIMEOUT = os.getenv("google_pub_sub_timeout", 2.0)

CONSUMER_TYPE = 'kafka'
KAFKA_HOST = os.getenv("kafka_host", "kafka:9092")
KAFKA_TOPIC = os.getenv("topic", "image-stream")
KAFKA_MIN_COMMIT_COUNT = os.getenv("kafka_min_commit_count", 5)
