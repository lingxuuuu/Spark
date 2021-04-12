import os
from pyspark.sql import SparkSession

os.environ['SPARK_HOME']="/home/hadoop/spark"

spark = SparkSession.builder.appName("Json_DF").master("local[*]").getOrCreate()

#spark.sparkContext.setLogLevel('ERROR')

json_df = spark.read.format("json").option("inferSchema","true").load("file:///home/hadoop/datasets/world_bank.json")

#json_df.printSchema()

#print(dict(json_df.dtypes["sector"]))

#print(json_df.dtypes)

print(dict(json_df.dtypes)['sector'])

json_df.show()