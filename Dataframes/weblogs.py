import os
import re

os.environ["SPARK_HOME"] = "/home/hadoop/spark"

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("weblog_prac").master("local[*]").getOrCreate()

sc = spark.sparkContext

raw_data = sc.textFile("file:////home/hadoop/datasets/weblogs/2013-09-15.log")

print(raw_data.take(1))

def extract_data(record):
    ip_pattern = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
    ip_addr = ip_pattern.match(record).group(0)

    # ts_pattern = re.compile(r"\d{1,2}/(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/\d{4}:\d{2}:\d{2}:\d{2}\s{1}([+]|[-])\d{4}")
    # ts = ts_pattern.search(record).group(0)

    ts_pattern = re.compile(r'\d{1,2}/(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)/\d{4}:\d{2}:\d{2}:\d{2}\s{1}[(+)|(-)]\d{1,4}')
    ts=ts_pattern.search(record).group(0)

    return ip_addr,ts

#print(extract_data('3.94.78.5 - 69827 [15/Sep/2013:23:58:36 +0100] "GET /KBDOC-00033.html HTTP/1.0" 200 14417 "http://www.loudacre.com"  "Loudacre Mobile Browser iFruit 1"'))

data_ex = raw_data.map(lambda x:extract_data(x))

data_ex.collect()

df = data_ex.toDF(["ip","ts"])

df.createOrReplaceTempView("temp_table")

spark.sql(""" select * from temp_table limit 10 """).show()


#spark.sql(""" select ip, avg(ts) from temp_table group by ip""").show(50)
