import os
from pyspark.sql import SparkSession

from pyspark import SparkConf, SQLContext, HiveContext, SparkContext

os.environ["SPARK_HOME"] = "/home/hadoop/spark"

spark = SparkSession.builder.appName("Mysql_Spark_DF").master("local[*]").config("spark.jars","/home/hadoop/spark/jars/mysql-connector-java.jar").getOrCreate()

sc = spark.sparkContext

sqlc = SQLContext(sc)

print(sc)

# spark.set("spark.jars","/home/hadoop/spark/jars/postgresql-42.2.11.jar")


# df = spark.read \
#     .format("jdbc") \
#     .option("url", "jdbc:postgresql://localhost:5432/databasename") \
#     .option("dbtable", "tablename") \
#     .option("user", "username") \
#     .option("password", "password") \
#     .option("driver", "org.postgresql.Driver") \
#     .load()
#
# df.printSchema()

rdbms_df = spark.read \
    .format("jdbc") \
    .option('url', 'jdbc:mysql://localhost:3306/sakila') \
    .option('user', 'root') \
    .option('password', 'root') \
    .option('dbtable', 'country') \
    .load()

# parq_df.show(5)

rdbms_df.show(500)

