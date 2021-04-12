import os

from pyspark.sql import SparkSession

os.environ["SPARK_HOME"] = "/home/hadoop/spark"

spark = SparkSession.builder.appName("Hive_Spark_DF").master("local[*]").enableHiveSupport().getOrCreate()

csv_df = spark.read.format("csv").option("inferSchema","true").option("header","true").load("file:///home/hadoop/datasets/au-500.csv")

#print(csv_df.count())

#csv_df.show(5)

#sql = spark.sql("select * from test.temp").show()

csv_df.write.format("orc").saveAsTable("test.csv_df")