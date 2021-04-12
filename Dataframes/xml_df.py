import os
from pyspark.sql import SparkSession

os.environ['SPARK_HOME'] = "/home/hadoop/spark"

spark = SparkSession.builder.appName("XML_DF").master("local[*]").getOrCreate()

xml_df = spark.read.format("xml").option("rowTag","record").load("file:///home/hadoop/datasets/sample.xml")

xml_df.show()

xml_df.select("address","address.street").show()