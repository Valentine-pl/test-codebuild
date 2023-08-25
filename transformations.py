#transformations.py

from pyspark.sql.functions import lit

def transformation_func(df):
    df.withColumn("new_column", lit("new_value_good"))
    return df
