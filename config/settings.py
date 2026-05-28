import os
from dotenv import load_dotenv

load_dotenv()

# API
API_BASE_URL = os.getenv("API_BASE_URL", "https://v3.football.api-sports.io")
API_KEY = os.getenv("API_KEY", "")

# PostgreSQL
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
POSTGRES_DB = os.getenv("POSTGRES_DB", "sports_db")
POSTGRES_USER = os.getenv("POSTGRES_USER", "sports_user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")

# Kafka
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC_FIXTURES = os.getenv("KAFKA_TOPIC_FIXTURES", "fixtures")
KAFKA_TOPIC_SCORES = os.getenv("KAFKA_TOPIC_SCORES", "live_scores")

# Cassandra
CASSANDRA_HOSTS = os.getenv("CASSANDRA_HOSTS", "localhost").split(",")
CASSANDRA_KEYSPACE = os.getenv("CASSANDRA_KEYSPACE", "sports_streaming")

# Data paths
BRONZE_PATH = os.getenv("BRONZE_PATH", "data/bronze")
SILVER_PATH = os.getenv("SILVER_PATH", "data/silver")
GOLD_PATH = os.getenv("GOLD_PATH", "data/gold")
