Run the following lines of code to get the data
// download the required module to run shell commands within the notebook
import sys.process._
If you completed the Getting Started lab, then you should have the data downloaded and unzipped in the /resources/jupyterlab/labs/BD0211EN/LabData/ directory. Otherwise, please uncomment the last two lines of code in each of the following cells to download and unzip the data.

// download the data from the IBM Server
// this may take ~30 seconds depending on your internet speed
​
//"wget --quiet https://cocl.us/BD0211EN_Data" !
​
//println("Data Downloaded!")
// this may take ~30 seconds depending on your internet speed
​
//"unzip -q -o -d /resources/jupyterlab/labs/BD0211EN/ BD0211EN_Data" !
​
//println("Data Extracted!")
The data is in a folder called LabData. Let's list all the files in the data that we just downloaded and extracted.

// list the extracted files
"ls -1 /resources/jupyterlab/labs/BD0211EN/LabData" !
Now we are going to create an RDD file from the file README. This is created using the spark context ".textFile" just as in the previous lab. As we know the initial operation is a transformation, so nothing actually happens. We're just telling it that we want to create a readme RDD.

Run the code in the following cell. This was an RDD transformation, thus it returned a pointer to a RDD, which we have named as readme.

val readme = sc.textFile("/resources/jupyterlab/labs/BD0211EN/LabData/README.md")
Let’s perform some RDD actions on this text file. Count the number of items in the RDD using this command:

readme.count()
Let’s run another action. Run this command to find the first item in the RDD:

readme.first()
Now let’s try a transformation. Use the filter transformation to return a new RDD with a subset of the items in the file. Type in this command:

val linesWithSpark = readme.filter(line => line.contains("Spark"))
linesWithSpark.count()
Again, this returned a pointer to a RDD with the results of the filter transformation.

You can even chain together transformations and actions. To find out how many lines contains the word “Spark”, type in:

readme.filter(line => line.contains("Spark")).count()
More on RDD Operations
This section builds upon the previous section. In this section, you will see that RDD can be used for more complex computations. You will find the line from that readme file with the most words in it.

readme.map(line => line.split(" ").size).
                    reduce((a, b) => if (a > b) a else b)
There are two parts to this. The first maps a line to an integer value, the number of words in that line. In the second part reduce is called to find the line with the most words in it. The arguments to map and reduce are Scala function literals (closures), but you can use any language feature or Scala/Java library.

In the next step, you use the Math.max() function to show that you can indeed use a Java library instead. Import in the java.lang.Math library:

import java.lang.Math
Now run with the max function:

readme.map(line => line.split(" ").size).
        reduce((a, b) => Math.max(a, b))
Spark has a MapReduce data flow pattern. We can use this to do a word count on the readme file.

val wordCounts = readme.flatMap(line => line.split(" ")).
                        map(word => (word, 1)).
                        reduceByKey((a,b) => a + b)
Here we combined the flatMap, map, and the reduceByKey functions to do a word count of each word in the readme file.

To collect the word counts, use the collect action.

It should be noted that the collect function brings all of the data into the driver node. For a small dataset, this isacceptable but, for a large dataset this can cause an Out Of Memory error. It is recommended to use collect() for testing only. The safer approach is to use the take() function e.g. take(n).foreach(println)
wordCounts.collect().foreach(println)
You can also do:

println(wordCounts.collect().mkString("\n"))

println(wordCounts.collect().deep)

YOUR TURN:
In the cell below, determine what is the most frequent CHARACTER in the README, and how many times was it used?
// WRITE YOUR CODE BELOW
​
​
​
Double-click here for the solution.

Analysing a log file
First, let's analyze a log file in the current directory.

val logFile = sc.textFile("/resources/jupyterlab/labs/BD0211EN/LabData/notebook.log")
Filter out the lines that contains INFO (or ERROR, if the particular log has it)

val info = logFile.filter(line => line.contains("INFO"))
Count the lines:

info.count()
Count the lines with Spark in it by combining transformation and action.

info.filter(line => line.contains("spark")).count()
Fetch those lines as an array of Strings

info.filter(line => line.contains("spark")).collect() foreach println
Remember that we went over the DAG. It is what provides the fault tolerance in Spark. Nodes can re-compute its state by borrowing the DAG from a neighboring node. You can view the graph of an RDD using the toDebugString command.

println(info.toDebugString)
Joining RDDs
Next, you are going to create RDDs for the README and the POM file in the current directory.

val readmeFile = sc.textFile("/resources/jupyterlab/labs/BD0211EN/LabData/README.md")
val pom = sc.textFile("/resources/jupyterlab/labs/BD0211EN/LabData/pom.xml")
How many Spark keywords are in each file?

println(readmeFile.filter(line => line.contains("Spark")).count())
println(pom.filter(line => line.contains("Spark")).count())
Now do a WordCount on each RDD so that the results are (K,V) pairs of (word,count)

val readmeCount = readmeFile.
                    flatMap(line => line.split(" ")).
                    map(word => (word, 1)).
                    reduceByKey(_ + _)
​
val pomCount = pom.
                flatMap(line => line.split(" ")).
                map(word => (word, 1)).
                reduceByKey(_ + _)
To see the array for either of them, just call the collect function on it.

println("Readme Count\n")
readmeCount.collect() foreach println
println("Pom Count\n")
pomCount.collect() foreach println
Now let's join these two RDDs together to get a collective set. The join function combines the two datasets (K,V) and (K,W) together and get (K, (V,W)). Let's join these two counts together and then cache it.

val joined = readmeCount.join(pomCount)
joined.cache()
Let's see what's in the joined RDD.

joined.collect.foreach(println)
Let's combine the values together to get the total count. The operations in this command tells Spark to combine the values from (K,V) and (K,W) to give us(K, V+W). The ._ notation is a way to access the value on that particular index of the key value pair.

val joinedSum = joined.map(k => (k._1, (k._2)._1 + (k._2)._2))
joinedSum.collect() foreach println
To check if it is correct, print the first five elements from the joined and the joinedSum RDD

println("Joined Individial\n")
joined.take(5).foreach(println)
​
println("\n\nJoined Sum\n")
joinedSum.take(5).foreach(println)
Shared variables
Broadcast variables allow the programmer to keep a read-only variable cached on each worker node rather than shipping a copy of it with tasks. They can be used, for example, to give every node a copy of a large input dataset in an efficient manner. After the broadcast variable is created, it should be used instead of the value v in any functions run on the cluster so that v is not shipped to the nodes more than once. In addition, the object v should not be modified after it is broadcast in order to ensure that all nodes get the same value of the broadcast variable (e.g. if the variable is shipped to a new node later).

Read more here: http://spark.apache.org/docs/latest/programming-guide.html#broadcast-variables

Let's create a broadcast variable:

Did you know? IBM Watson Studio lets you build and deploy an AI solution, using the best of open source and IBM software and giving your team a single environment to work in. Learn more here.
val broadcastVar = sc.broadcast(Array(1,2,3))
To get the value, type in:

broadcastVar.value
Accumulators are variables that can only be added through an associative operation. It is used to implement counters and sum efficiently in parallel. Spark natively supports numeric type accumulators and standard mutable collections. Programmers can extend these for new types. Only the driver can read the values of the accumulators. The workers can only invoke it to increment the value.

Create the accumulator variable. Type in:

val accum = sc.accumulator(0)
Next parallelize an array of four integers and run it through a loop to add each integer value to the accumulator variable. Type in:

sc.parallelize(Array(1,2,3,4)).foreach(x => accum += x)
To get the current value of the accumulator variable, type in:

accum.value
You should get a value of 10. This command can only be invoked on the driver side. The worker nodes can only increment the accumulator.

Key-value pairs
You have already seen a bit about key-value pairs in the Joining RDD section. Here is a brief example of how to create a key-value pair and access its values. Remember that certain operations such as map and reduce only works on key-value pairs.

Create a key-value pair of two characters. Type in:

val pair = ('a', 'b')
To access the value of the first index using the .1_ method and .2_ method for the 2nd.

pair._1
pair._2
Sample Application
In this section, you will be using a subset of a data for taxi trips that will determine the top 10 medallion numbers based on the number of trips.

val taxi = sc.textFile("/resources/jupyterlab/labs/BD0211EN/LabData/nyctaxi.csv")
To view the five rows of content, invoke the take function. Type in:

taxi.take(5).foreach(println)
Note that the first line is the headers. Normally, you would want to filter that out, but since it will not affect our results, we can leave it in.

To parse out the values, including the medallion numbers, you need to first create a new RDD by splitting the lines of the RDD using the comma as the delimiter. Type in:

val taxiParse = taxi.map(line=>line.split(","))
Now create the key-value pairs where the key is the medallion number and the value is 1. We use this model to later sum up all the keys to find out the number of trips a particular taxi took and in particular, will be able to see which taxi took the most trips. Map each of the medallions to the value of one. Type in:

val taxiMedKey = taxiParse.map(vals=>(vals(6), 1))
vals(6) corresponds to the column where the medallion key is located

Next use the reduceByKey function to count the number of occurrence for each key.

val taxiMedCounts = taxiMedKey.reduceByKey((v1,v2)=>v1+v2)
​
taxiMedCounts.take(5).foreach(println)
Finally, the values are swapped so they can be ordered in descending order and the results are presented correctly.

for (pair <-taxiMedCounts.map(_.swap).top(10)) println("Taxi Medallion %s had %s Trips".format(pair._2, pair._1))
While each step above was processed one line at a time, you can just as well process everything on one line:

val taxiMedCountsOneLine = taxi.map(line=>line.split(',')).map(vals=>(vals(6),1)).reduceByKey(_ + _)
Run the same line as above to print the taxiMedCountsOneLine RDD.

for (pair <-taxiMedCountsOneLine.map(_.swap).top(10)) println("Taxi Medallion %s had %s Trips".format(pair._2, pair._1))
Let's cache the taxiMedCountsOneLine to see the difference caching makes. Run it with the logs set to INFO and you can see the output of the time it takes to execute each line. First, let's cache the RDD

taxiMedCountsOneLine.cache()
Next, you have to invoke an action for it to actually cache the RDD. Note the time it takes here (either empirically using the INFO log or just notice the time it takes)

taxiMedCountsOneLine.count()
Run it again to see the difference.

taxiMedCountsOneLine.count()
The bigger the dataset, the more noticeable the difference will be. In a sample file such as ours, the difference may be negligible.

Tip: Enjoyed using Jupyter notebooks with Spark? Get yourself a free IBM Cloud account where you can use Data Science Experience notebooks and have two Spark executors for free!
Summary
Having completed this exercise, you should now be able to describe Spark’s primary data abstraction, understand how to create parallelized collections and external datasets, work with Resilient Distributed Dataset (RDD) operations, and utilize shared variables and key-value pairs.

This notebook is part of the free course on cognitiveclass.ai called Spark Fundamentals I. If you accessed this notebook outside the course, you can take this free self-paced course, online by going to: http://cocl.us/Spark_Fundamentals_I
