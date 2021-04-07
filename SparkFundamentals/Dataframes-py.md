A DataFrame is two-dimensional. Columns can be of different data types. DataFrames accept many data inputs including series and other DataFrames. 
You can pass indexes (row labels) and columns (column labels). Indexes can be numbers, dates, or strings/tuples.

Pandas is a library used for data manipulation and analysis. Pandas offers data structures and operations for creating and manipulating Data Series 
and DataFrame objects. Data can be imported from various data sources, e.g., Numpy arrays, Python dictionaries and CSV files. Pandas allows you to 
manipulate, organize and display the data. 

In this short notebook, we will load and explore the mtcars dataset. Specifically, this tutorial covers:

1.  Loading data in memory
2.  Creating SQLContext
3.  Creating Spark DataFrame
4.  Group data by columns 
5.  Operating on columns
6.  Running SQL Queries from a Spark DataFrame

## Loading in a DataFrame
To create a Spark DataFrame we load an external DataFrame, called mtcars. This DataFrame includes 32 observations on 11 variables:

[, 1] mpg Miles/(US) --> gallon
[, 2] cyl --> Number of cylinders
[, 3] disp --> Displacement (cu.in.)
[, 4] hp --> Gross horsepower
[, 5] drat --> Rear axle ratio
[, 6] wt --> Weight (lb/1000)
[, 7] qsec --> 1/4 mile time
[, 8] vs --> V/S
[, 9] am --> Transmission (0 = automatic, 1 = manual)
[,10] gear --> Number of forward gears
[,11] carb --> Number of carburetors

```
import pandas as pd
mtcars = pd.read_csv('https://cocl.us/BD0211EN_mtcars')
```
```
mtcars.head()
```

## Initialize SQLContext

To work with dataframes we need an SQLContext which is created using SQLContext(sc). SQLContext uses SparkContext which has been already created in Data Scientist
Workbench, named sc.

But first, let's import the tools that we need to use Spark in SN Labs.

```
!pip install findspark
!pip install pyspark
import findspark
import pyspark
findspark.init()
sc = pyspark.SparkContext.getOrCreate()
```
```
sqlContext = SQLContext(sc)
```

## Creating Spark DataFrames

With SQLContext and a loaded local DataFrame, we create a Spark DataFrame:

```
sdf = sqlContext.createDataFrame(mtcars) 
sdf.printSchema()
```

## Displays the content of the DataFrame
```
sdf.show(5)
```

## Selecting columns
```
sdf.select('mpg').show(5)
```

## Filtering Data

Filter the DataFrame to only retain rows with mpg less than 18

Did you know? IBM Watson Studio lets you build and deploy an AI solution, using the best of open source and IBM software and giving your team a single 
environment to work in. Learn more here.

```
sdf.filter(sdf['mpg'] < 18).show(5)
```
## Operating on Columns

SparkR also provides a number of functions that can be directly applied to columns for data processing and aggregation. The example below shows 
the use of basic arithmetic functions to convert lb to metric ton.

```
sdf.withColumn('wtTon', sdf['wt'] * 0.45).show(6)
sdf.show(6)
```

## Grouping, Aggregation
Spark DataFrames support a number of commonly used functions to aggregate data after grouping. For example we can compute the average weight of cars by 
their cylinders as shown below:

```
sdf.groupby(['cyl'])\
.agg({"wt": "AVG"})\
.show(5)
```
```
# We can also sort the output from the aggregation to get the most common cars
car_counts = sdf.groupby(['cyl'])\
.agg({"wt": "count"})\
.sort("count(wt)", ascending=False)\
.show(5)
```

## Running SQL Queries from Spark DataFrames
A Spark DataFrame can also be registered as a temporary table in Spark SQL and registering a DataFrame as a table allows you to run SQL queries over its data. 
The sql function enables applications to run SQL queries programmatically and returns the result as a DataFrame.

```
# Register this DataFrame as a table.
sdf.registerTempTable("cars")

# SQL statements can be run by using the sql method
highgearcars = sqlContext.sql("SELECT gear FROM cars WHERE cyl >= 4 AND cyl <= 9")
highgearcars.show(6)   
NOTE: This tutorial draws heavily from the original Spark Quick Start Guide
```

## Summary
Having completed this exercise, you should now be able to load data in memory, create SQLContext, create Spark DataFrame, group data by columns, and run SQL Queries 
from a Spark dataframe.

This notebook is part of the free course on cognitiveclass.ai called Spark Fundamentals I. If you accessed this notebook outside the course, you can take this 
free self-paced course, online by going to: http://cocl.us/Spark_Fundamentals_I

