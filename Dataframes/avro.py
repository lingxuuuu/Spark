import os
from pyspark.sql import SparkSession

os.environ['SPARK_HOME'] = "/home/hadoop/spark"

spark = SparkSession.builder.appName("AVRO_DF").master("local[*]").getOrCreate()

avro_df = spark.read.format("avro").load("file:///home/hadoop/datasets/avro_files/userdata1.avro")

avro_df.show(10)