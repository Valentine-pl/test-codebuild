#transformations.py

from pyspark.sql.functions import lit

def transformation_func(df):
    df = df.withColumn("new_column1", lit("new_value1"))
    return df
