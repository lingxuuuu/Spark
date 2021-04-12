import os
from pyspark.sql import SparkSession

os.environ["SPARK_HOME"] = "/home/hadoop/spark"

#spark = SparkSession.builder.appName("Mysql_Spark_DF").master("local[*]").config("spark.jars","/home/hadoop/spark/jars/mongo-spark-connector_2.11-2.4.1.jar").getOrCreate()

spark = SparkSession.builder.appName("Mysql_Spark_DF")\
    .config("spark.mongodb.input.uri", "mongodb://localhost/mydb.users") \
    .config("spark.mongodb.output.uri", "mongodb://localhost/mydb.users") \
    .master("local[*]").getOrCreate()

df = spark.read.format("mongo").load()

df.show()

