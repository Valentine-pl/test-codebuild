#transformations.py

from pyspark.sql.functions import lit

def transformation_func(df):
    return df.withColumn("new_column", lit("new_value_super"))
