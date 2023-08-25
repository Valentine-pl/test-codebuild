#transformations.py

from pyspark.sql.functions import lit

def transformation_func(df):
    #df = df.withColumn("new_column1", lit("new_value1"))
    df = df.withColumn("new_column2", lit("new_value2"))
   # Drop the column 'new_column1'
    df = df.drop("new_column1")
    return df
