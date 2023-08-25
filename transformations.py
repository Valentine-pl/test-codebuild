#transformations.py

from pyspark.sql.functions import lit

def transformation_func(df):
    df.withColumn("new_column", lit("new_value_good"))
    df.withColumn("new_column2", lit("new_value_2"))
    return df
