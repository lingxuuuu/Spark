import os
from pyspark.sql import SparkSession

os.environ["SPARK_HOME"] = "/home/hadoop/spark"

spark = SparkSession.builder.appName("Parquet_DF").master("local[*]").getOrCreate()


parq_df = spark.read.load("file:///home/hadoop/datasets/parquet_files")

#parq_df.show(5)

parq_df.printSchema()

print(parq_df.schema)