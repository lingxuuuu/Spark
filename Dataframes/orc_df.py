import os
from pyspark.sql import SparkSession

#from pyspark.sql.types import StructType, StructField,IntegerType,TimestampType,StringType,DoubleType

from pyspark.sql.types import *
os.environ["SPARK_HOME"] = "/home/hadoop/spark"

spark = SparkSession.builder.appName("Parquet_DF").master("local[*]").getOrCreate()

# orc_df = spark.read.format("orc").load("file:///home/hadoop/datasets/orc_filles")
#
# orc_df.printSchema()
#
# print(orc_df.show(5))

orc_schema =StructType([
                        StructField("registration_dttm",TimestampType(),True),
                            StructField("id",IntegerType(),True),
                            StructField("first_name",StringType(),True),
                            StructField("last_name",StringType(),True),
                            StructField("email",StringType(),True),
                            StructField("gender",StringType(),True),
                            StructField("ip_address",StringType(),True),
                            StructField("cc",StringType(),True),
                            StructField("country",StringType(),True),
                            StructField("birthdate",StringType(),True),
                            StructField("salary",DoubleType(),True),
                            StructField("title",StringType(),True),
                            StructField("comments",StringType(),True)])


orc_df = spark.read.format("orc").schema(orc_schema).load("file:///home/hadoop/datasets/orc_filles")

print(orc_df.show(5))
