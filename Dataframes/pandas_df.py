import os
from pyspark.sql import SparkSession
import pandas as pd

os.environ['SPARK_HOME'] = "/home/hadoop/spark"

spark = SparkSession.builder.appName("PANDAS_DF").master("local[*]").getOrCreate()

pandas_df = pd.DataFrame([{"name":"abc", "score":2.0},{"name":"xyz", "score":3.5}])

print(type(pandas_df))

spark_pandas_df = spark.createDataFrame(pandas_df)

print(spark_pandas_df)

spark_pandas_df.show()