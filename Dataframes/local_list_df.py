import os
from pyspark.sql import SparkSession

os.environ["SPARK_HOME"] = "/home/hadoop/spark"

spark = SparkSession.builder.appName("CSV_DF").master("local[*]").getOrCreate()

sc = spark.sparkContext
l1 = [("hadoop",3.0),("spark",2.4),("hive",3.0)]

schema = ["comp","ver"]

l2 = sc.parallelize(l1).toDF(schema)

l2.show()