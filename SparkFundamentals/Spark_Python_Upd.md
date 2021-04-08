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

-------------------------------------------------------------------------------------------------------------------

