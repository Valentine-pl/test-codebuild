from spark_config import spark
from transformations import transformation_func

s3_path = "s3a://vp-test-coudbuilder/data/faker_database/faker_csv/"
data =  spark.read.csv(s3_path, header=True, inferSchema=True)

# Apply the transformation
df_transformed = transformation_func(data)

# Write the transformed data to Parquet format locally (you can adjust the path as needed)
output_path = "s3a://vp-test-coudbuilder/data/faker_database/faker_parquet/"
df_transformed.write \
    .mode("append") \
    .partitionBy("year", "month", "day", "hour", "minute") \
    .parquet(output_path, compression="snappy")

spark.stop()