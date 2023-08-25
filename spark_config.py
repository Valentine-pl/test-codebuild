#spark_config.py
from pyspark.sql import SparkSession
from aws_config import AWS_ACCESS_KEY_ID, AWS_DEFAULT_REGION, AWS_SECRET_ACCESS_KEY

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("CSV to Parquet") \
    .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.1") \
    .getOrCreate()

# Configure S3 access
spark.conf.set("spark.hadoop.fs.s3a.access.key", AWS_ACCESS_KEY_ID)
spark.conf.set("spark.hadoop.fs.s3a.secret.key", AWS_SECRET_ACCESS_KEY)
spark.conf.set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
spark.conf.set("spark.hadoop.fs.s3a.path.style.access", True)