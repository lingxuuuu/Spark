# Pyspark

__Spark using Python__

* Spark was developed in the year 2009
* It was open source in the year 2010
* It was donate to apache in the year 2013

__DEF__

spark is a
     -Distributed Execution framework 
     -in parallelel process style
     -with in-memmory computing feature
     -used for large-scale data processing

spark can be coded with
  i)scala
 ii)python
 iii)Java
 iv)R language

Spark can run on Distributed clusters like
i)Yarn
ii)AWS
iii)mesos

Spark can also run on stand-alone cluster

YARN------> distributed computing model/cluster

Spark is an execution model:

 Here we develop applications based on bussiness logic when apllication is ready , we need to deploy our application on a distributed computing cluster such as 
 YARN ,here our application is going to run


Hadoop-----> meant for
     i)storage------------------>HDFS
    ii)Processing--------------->Map Reduce, here we have drawbacks, so replace with spark


Hadoop meant for batch processing:

Batch processing: On huge data(static)----------> applying B.L an processing it

Streaming process : 2 steps
  i)Data Ingestion(DI) : Here nothing but capturing data
 ii)Data Processing(DP): processing the captured data

here Data Injestion and Data Processing both should happen parallelly---> that is what streaming

Data Ingestion : pulling data from external sources to Target HDFS

Hadoop and spark both performs Batch processing

In Hadoop------->Data Ingestion----->then Data Processing--->done sequentially

In streaming process------>Data Ingestion an Data Processing---->both happens parallely
                           here processing should be very fast , we should get results in secs
                           here expecting the results immediately

But in batch process------> we cannot expect the results immediately
ex: MR-------> speed cannot reach the streaming process
 at one side keeps on capturing very fast
 but the other side--->processing is slow as compared with capturing

so go with spark, which can reach the speed of capturing 
Spark 100 times faster than MR in memory------->given by DataBricks ,who developed spark

MR cannot produce results in secs
Spark can produce results in secs


data-------> HDFS-------> processed by MR   -------> here MR application to run-------> we require a Distributed cluster
                -------> Processed by spark

for MR------>Distribute cluster such as YARN is mandatory

MR can run only on YARN distributed cluster

But spark can run on distributed clusters such as, 
                i)YARN  (not manddatory)
                ii)AWS
                iii)Mesos
                iv)Kubernotes
Spark can also run on spark stand alone cluster

so spark can run on many distributed clusters, but MR can run only on YARN cluster

----------------------------------------------------------------------------------------------------------
              storage       processing

MR-----------> HDFS --------> YARN
spark--------> HDFS---------> YARN
              AWS(s3)------> EC2---> Elastic computing cloud


In MR, data should be within HDFS
but for spark it can be not only in HDFS but in other environments also

spark can pull data from 
1)HDFS /LFS /NFS (N/w file system)
2)Database like mysql, oracle, Teradata etc
3)AWS s3
4)NOsql------> hbase, cassandra, mongodb
5)flume
6)kafka
7)kinesis

Spark can be integrated with any of the above mentioned

-----------------------------------------------------------------------------------------------------------
Programming Languages supported by spark
1)Scala API
2)Python API
3)Java API
4)R  API

----------------------------------------------------------------------------------------------------------
## python API

__Advantages of python:__

Python was built or derived by taking features or advantages from various other programming languages
such as
 i)Functional programming (or) procedural-oriented programming ex: C
 ii)Object-Oriented Programming  ex: c++, Java
 iii)Scripting language  ex: shell scripting
 iv)Modular programming  ex: modula-3 ----------->89,300 modules 

Because of these multiple features, we call python as hybrid language

ex:

Defining a variable

   JAVA             SCALA             PYTHON
  int x=10        val x=10            x=10

89,300 modules supported by python
Datascience---------> seperated modules
Machine Learing------>   "
BigData ------------->   "
Networking------------>  "
Graphics (GUI)-------->  "
Operating systems------>  "
oracle ----------------> "
mysql------------------->  "
xml ---------------------> "
json --------------------> "
csv ---------------------> "
Testing------------------> "
math --------------------> "


------------------------------------------------------------

## 3 ways to create a RDD:

I: whenever u load a file from hdfs using sparkContext(sc) then the result is a RDD

$ hdfs dfs -put emp7 /pysparklab
lenovo@lenovo-Lenovo-G450:~$ hdfs dfs -cat /pysparklab/emp7
101,miller,10000,m,11,
102,Blake,20000,m,12,
103,sony,30000,f,11,
104,sita,40000,f,12,
105,John,50000,m,13

>>> r1=sc.textFile("hdfs://localhost:9000/pysparklab/emp7")
>>> r1.collect()
>>>

[u'101,miller,10000,m,11,', u'102,Blake,20000,m,12,', u'103,sony,30000,f,11,', u'104,sita,40000,f,12,', u'105,John,50000,m,13']

-------------------------------------------------------------------------------------------------------
II: whenever we parallelize any python/scala/java object-----> result is a RDD 

>>> x=[10,20,30,40,50]
>>> r2=sc.parallelize(x)
>>> r2.collect()
[10, 20, 30, 40, 50]

-----------------------------------------------------------------------------------------------------
working with map() : map() cant be applied on python list , its not a member of python list
                     map() can be applied on a RDD

ex:Incrementing each element of list by 5
>>> l1=[10,20,30,40,50]
>>> res=l1.map(x=>x+5)
  File "<stdin>", line 1
    res=l1.map(x=>x+5)
                 ^
SyntaxError: invalid syntax
---------------------------------------------------
ex:2
>>> res=l1.map(lambda x:x+5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'map'
-----------------------------------------------------


III-way: whenevever we perform transformations/Actions on a RDD------->Resultant also is a RDD

>>> l1=[10,20,30,40,50]
>>> r3=sc.parallelize(l1)
>>> r4=r3.map(x=>x+5)
  File "<stdin>", line 1
    r4=r3.map(x=>x+5)
                ^
SyntaxError: invalid syntax

so go with lambda function
>>> r4=r3.map(lambda x:x+5)
>>> r4.collect()
[15, 25, 35, 45, 55]   

here r4 is a RDD

-------------------------------------------------------------------------------------------------------------

## On a RDD , we can apply 2 things

i)Transformations
ii)Actions


1)Transformations: 3 types
 i)Each element Transformation 
   ex: map(), flatMap()
       RDD.map(.....)
       RDD.flatMap(....)
 
 ii)Filter Transformation
    ex:RDD.filter(...)

 iii)Aggregated Transformation:
     ex: reduceByKey(),
         groupByKey()
         rdd.reduceByKey(_+_)
         rdd.groupByKey( )
         
-------------------------------------------------------------------------------------------------------------

# Various Transformations:

1.map()
2.flatMap()
3.filter()
4.union()
5.intersection()
6.substract()
7.cartesian()
8.distinct()

1)map(): Applying operation to each element of a RDD and returns a RDD.

>>> r1=sc.parallelize([10,20,30,40,50])
>>> # to square each element of a RDD
... 
>>> r2=r1.map(lambda x:x*x)
>>> r2.collect()
[100, 400, 900, 1600, 2500]    

--------------------------------------------------------------------------------------
2)flatMap(): Flattens the elements

>>> x=[[10,20,30],[40,50,60]]
>>> y=sc.parallelize(x)
>>> z=y.flatMap(lambda x:x)
>>> z.collect()
[10, 20, 30, 40, 50, 60]

ex:2

>>> x=[[10,20,30],[40,50,60],[70,80,90]
... ]
>>> y=sc.parallelize(x)
>>> z=y.flatMap(lambda x:x)
>>> z.collect()
[10, 20, 30, 40, 50, 60, 70, 80, 90]

--------------------------------------------------------------------------------------
3)filter(): filters elements of a RDD based on condition and returns a RDD

>>> a=[10,20,30,40,50]
>>> b=sc.parallelize(a)
>>> res=b.filter(lambda x:x>=30)
>>> res.collect()
[30, 40, 50]

ex:2

>>> a=["java","python","hadoop","spark","devops"]
>>> b=sc.parallelize(a)
>>> # filter those other than java
... 
>>> res=b.filter(lambda x:x!="java")
>>> res.collect()
['python', 'hadoop', 'spark', 'devops']

--------------------------------------------------------------------------------------
4)union(): Combines elements of multiple RDDs  
           by default performs union all operation (allows duplicates)

>>> r1=sc.parallelize([10,20,30,40,50])
>>> r2=sc.parallelize([10,20,60,70,80])
>>> res=r1.union(r2)
>>> res.collect()
[10, 20, 30, 40, 50, 10, 20, 60, 70, 80]         

---------------------------------------------------------------------------------------
5)intersection: returns only the common elements
>>> res1=r1.intersection(r2)
>>> res1.collect()
[20, 10]     
--------------------------------------------------------------------------------------
6)substract() : removes common elements from a RDD
>>> res2=r1.subtract(r2)
>>> res2.collect()
[40, 50, 30] 

--------------------------------------------------------------------------------------
7)cartesian() : performs cartesian product with other RDD
                Each element of left RDD will join with each element of Right RDD

>>> r1=sc.parallelize(["hadoop","spark","python"])
>>> r2=sc.parallelize([1,2,3])
>>> res4=r1.cartesian(r2)
>>> res4.collect()
[('hadoop', 1), ('hadoop', 2), ('hadoop', 3), ('spark', 1), ('python', 1), ('spark', 2), ('spark', 3), ('python', 2), ('python', 3)]

----------------------------------------------------------------------------------------
8)distinct(): Eliminates the duplicates

>>> r1=sc.parallelize(["java","hadoop","python","spark","hadoop","java","python"])
>>> res5=r1.distinct()
>>> res5.collect()
['python', 'spark', 'java', 'hadoop'] 

----------------------------------------------------------------------------------------

## Transformations on a pair RDD(k,v) pairs:

1)reduceByKey()
2)groupByKey()
3)sortByKey()
4)mapValues()
5)keys()
6)values()
7)join()
8)leftOuterJoin()
9)rightOuterJoin()
10)fullOuterJoin()

---------------------------------------------------------------------------------------
1)reduceByKey() : sum up the values with same key

>>> r1=sc.parallelize([(11,10000),(12,20000),(13,30000),(11,40000),(12,50000),(13,60000),(11,35000)])
>>> res=r1.reduceByKey(lambda x,y:x+y)
>>> res.collect()
[(12, 70000), (11, 85000), (13, 90000)]  

--------------------------------------------------------------------------------------
2)groupByKey(): groups values with the same key

>>> r1=sc.parallelize([(11,10000),(12,20000),(13,30000),(11,40000),(12,50000),(13,60000),(11,35000)])
>>> res1=r1.groupByKey()
>>> res1.collect()
[(12, <pyspark.resultiterable.ResultIterable object at 0x7f14f091e490>), (11, <pyspark.resultiterable.ResultIterable object at 0x7f14f091e950>), (13, <pyspark.resultiterable.ResultIterable object at 0x7f14f08b8fd0>)]

here we get iterable object(combact buffer) , convert this into list and access the list

>>> res2=res1.map(lambda x:(x[0],list(x[1])))
>>> res2.collect()
[(12, [10000, 50000]), (11, [10000, 40000, 35000]), (13, [30000, 60000])]

---------------------------------------------------------------------------------------------------
3)sortByKey():sorting based on key

>>> r1=sc.parallelize([(11,10000),(12,20000),(13,30000),(11,40000),(12,50000),(13,60000),(11,35000)])
>>> res=r1.sortByKey()
>>> res.collect()
[(11, 10000), (11, 40000), (11, 35000), (12, 20000), (12, 50000), (13, 30000), (13, 60000)]

------------------------------------------------------------------------------------------------------
4)mapValues() :Applying a functionality to each value without changing the key

>>> r1=sc.parallelize([(11,10000),(12,20000),(13,30000),(11,40000),(12,50000),(13,60000),(11,35000)])
>>> res=r1.mapValues(lambda x:x+5000)
>>> res.collect()
[(11, 15000), (12, 25000), (13, 35000), (11, 45000), (12, 55000), (13, 65000), (11, 40000)]

------------------------------------------------------------------------------------------------------
5)keys(): Returns the keys of RDDs
>>> r1=sc.parallelize([(11,10000),(12,20000),(13,30000),(11,40000),(12,50000),(13,60000),(11,35000)])
>>> res=r1.keys()
>>> res.collect()
[11, 12, 13, 11, 12, 13, 11]

-----------------------------------------------------------------------------------------------------
6)values(): returns the values of RDD
>>> r1=sc.parallelize([(11,10000),(12,20000),(13,30000),(11,40000),(12,50000),(13,60000),(11,35000)])
>>> res=r1.values()
>>> res.collect()
[10000, 20000, 30000, 40000, 50000, 60000, 35000]
-----------------------------------------------------------------------------------------------------
7)joins:

>>> r1=sc.parallelize([(10,20),(30,40),(50,60)])
>>> r2=sc.parallelize([(10,20),(30,40),(70,80)])
>>> ij=r1.join(r2)
>>> ij.collect()
[(10, (20, 20)), (30, (40, 40))]                                                
>>> 
>>> loj=r1.leftOuterJoin(r2)
>>> loj.collect()
[(10, (20, 20)), (50, (60, None)), (30, (40, 40))]                              
>>> 
>>> roj=r1.rightOuterJoin(r2)
>>> roj.collect()
[(10, (20, 20)), (70, (None, 80)), (30, (40, 40))]                              
>>> 
>>> foj=r1.fullOuterJoin(r2)
>>> foj.collect()
[(10, (20, 20)), (70, (None, 80)), (50, (60, None)), (30, (40, 40))]  

----------------------------------------------------------------------------------------------------------

# Actions: Whenever action is performed , the flow executes from its root RDD

The following are the various actions:

1)collect()
2)count()
3)countByValue()
4)countByKey()
5)take(num)
6)top(num)
7)first()
8)reduce()
9)sum()
10)max()
11)min()
12)count()
13)saveAsTextFile(path)

-----------------------------------------------------------------------------------------------------
1)collect() : It will collect all partitions data of different slave machines into client
>>> x=[10,20,30,40,50,60]
>>> r1=sc.parallelize(x)
>>> r1.collect()
[10, 20, 30, 40, 50, 60]

---------------------------------------------------------------------------------------------------
2)count() : counts no of elements in a RDD
>>> r1.count()
6

---------------------------------------------------------------------------------------------------
3)countByValue() : counts no of times each value occurs in a RDD.
                   we get o/p in the form of dictionary(key:value)
                   applied on a RDD
>>> x=["hadoop","java","spark","python","spark","java","hadoop","python","hadoop","spark"]
>>> r1=sc.parallelize(x)
>>> r1.countByValue()
defaultdict(<type 'int'>, {'python': 2, 'spark': 3, 'java': 2, 'hadoop': 3})

ex:2
>>> sals=[10000,20000,30000,10000,20000,30000,40000,50000,10000]
>>> r1=sc.parallelize(sals)
>>> r1.countByValue()
defaultdict(<type 'int'>, {10000: 3, 20000: 2, 40000: 1, 50000: 1, 30000: 2})

----------------------------------------------------------------------------------------------------
4)countByKey() :counts no of times each key had occured
                we get o/p in the form of dictionary(key:value)
                should be applied on a paired RDD
>>> x=[("IND","sachin"),("Aus","warner"),("WI","Lara"),("IND","Dravid"),("Aus","smith"),("SA","miller"),("IND","Ganguly")]
>>> r1=sc.parallelize(x)
>>> r1.countByKey()
defaultdict(<type 'int'>, {'IND': 3, 'Aus': 2, 'SA': 1, 'WI': 1})

-----------------------------------------------------------------------------------------------------
5)take(n) : takes first 'n' elements of a RDD.
>>> names=["Ajay","Rohin","miller","David","smith","James"]
>>> r1=sc.parallelize(names)
>>> r1.take(3)
['Ajay', 'Rohin', 'miller']

ex:2
>>> x=[10,20,30,40,50]
>>> r1=sc.parallelize(x)
>>> r1.take(3)
[10, 20, 30]

>>> r2=r1.take(3)
>>> r2.take(2)

AttributeError: 'list' object has no attribute 'take'
Error bcoz r2 is not a RDD ,only on RDD, we perform Actions , but r2 is a python object(list)
>>> r3=sc.parallelize(r2)
>>> r3.take(2)
[10, 20]

-------------------------------------------------------------------------------------------------------
6)top(n): takes top 'n' no of elements
>>> x=[10,20,30,40,50]
>>> r1=sc.parallelize(x)
>>> r1.top(3)
[50, 40, 30]

------------------------------------------------------------------------------------------------------
7)first() : Takes 1st element of a RDD
>>> x=[10,20,30,40,50]
>>> r1=sc.parallelize(x)
>>> r1.first()
10
-----------------------------------------------------------------------------------------------------
8)reduce() :combines or sums elements of a RDD
>>> x=[10,20,30,40,50]
>>> r1=sc.parallelize(x)
>>> r1.reduce(lambda x,y:x+y)
150

-----------------------------------------------------------------------------------------------------
9)sum(): finds sum of RDD elements
>>> x=[10,20,30,40,50]
>>> r1=sc.parallelize(x)
>>> r1.sum()
150     

---------------------------------------------------------------------------------------------------
10)max() : finds max element of a RDD
>>> r1.max()
50
--------------------------------------------------------------------------------------------------
11)min() :finds min element of a RDD
>>> r1.min()
10
------------------------------------------------------------------------------------------------
11)count() : finds the count i.e no of elements of a RDD.
>>> r1.count()
5
-----------------------------------------------------------------------------------------------
12)saveAsTextFile(path) : saving the output of a RDD as text file into specified path

>>> x=[10,20,30,40,50]
>>> r1=sc.parallelize(x)
>>> r2=r1.map(lambda x:x+5)
>>> r2.collect()
[15, 25, 35, 45, 55]  

I want to save this r2 o/p into hdfs
>>> r2.saveAsTextFile("hdfs://localhost:9000/pysparklab/res1")
>>>              

lenovo@lenovo-Lenovo-G450:~$ hdfs dfs -ls /pysparklab/res1
Found 3 items
-rw-r--r--   1 lenovo supergroup          0 2019-02-08 18:50 /pysparklab/res1/_SUCCESS
-rw-r--r--   1 lenovo supergroup          6 2019-02-08 18:50 /pysparklab/res1/part-00000
-rw-r--r--   1 lenovo supergroup          9 2019-02-08 18:50 /pysparklab/res1/part-00001
lenovo@lenovo-Lenovo-G450:~$ hdfs dfs -cat /pysparklab/res1/part-00000
15
25
lenovo@lenovo-Lenovo-G450:~$ hdfs dfs -cat /pysparklab/res1/part-00001
35
45
55
