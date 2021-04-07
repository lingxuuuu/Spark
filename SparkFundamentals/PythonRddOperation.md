## Analyzing a log file

Now, let's create an RDD by loading the log file that we analyze in the Scala version of this lab.

logFile = sc.textFile("/resources/jupyterlab/labs/BD0211EN/LabData/notebook.log")
info = logFile.filter(lambda line: "INFO" in line)

​
Count the lines:
info.count()
​
​

Count the lines with "spark" in it by combining transformation and action.
info.filter(lambda line: "spark" in line).count()
​
​

Fetch those lines as an array of Strings
info.filter(lambda line: "spark" in line).collect()
​

View the graph of an RDD using this command:

print(info.toDebugString())

## Joining RDDs

Next, you are going to create RDDs for the same README and the POM files that we used in the Scala version.

readmeFile = sc.textFile("/resources/jupyterlab/labs/BD0211EN/LabData/README.md")

pomFile = sc.textFile("/resources/jupyterlab/labs/BD0211EN/LabData/pom.xml")

How many Spark keywords are in each file?

print(readmeFile.filter(lambda line: "Spark" in line).count())
print(pomFile.filter(lambda line: "Spark" in line).count())

Now do a WordCount on each RDD so that the results are (K,V) pairs of (word,count)

readmeCount = readmeFile.                    \
    flatMap(lambda line: line.split("   ")).   \
    map(lambda word: (word, 1)).             \
    reduceByKey(lambda a, b: a + b)
    
pomCount = pomFile.                          \
    flatMap(lambda line: line.split("   ")).   \
    map(lambda word: (word, 1)).            \
    reduceByKey(lambda a, b: a + b)
    
To see the array for either of them, just call the collect function on it.

print("Readme Count\n")
print(readmeCount.collect())
print("Pom Count\n")
print(pomCount.collect())

The join function combines the two datasets (K,V) and (K,W) together and get (K, (V,W)). Let's join these two counts together.

joined = readmeCount.join(pomCount)
Print the value to the console

joined.collect()

Let's combine the values together to get the total count

joinedSum = joined.map(lambda k: (k[0], (k[1][0]+k[1][1])))

To check if it is correct, print the first five elements from the joined and the joinedSum RDD

print("Joined Individial\n")
print(joined.take(5))
​
print("\n\nJoined Sum\n")
print(joinedSum.take(5))

## Shared variables
Normally, when a function passed to a Spark operation (such as map or reduce) is executed on a remote cluster node, it works on separate copies of all the 
variables used in the function. These variables are copied to each machine, and no updates to the variables on the remote machine are propagated back to 
the driver program. Supporting general, read-write shared variables across tasks would be inefficient. However, Spark does provide two limited types of 
shared variables for two common usage patterns: broadcast variables and accumulators.

## Broadcast variables
Broadcast variables are useful for when you have a large dataset that you want to use across all the worker nodes. A read-only variable is cached on each 
machine rather than shipping a copy of it with tasks. Spark actions are executed through a set of stages, separated by distributed “shuffle” operations. 
Spark automatically broadcasts the common data needed by tasks within each stage.

Read more here: http://spark.apache.org/docs/latest/programming-guide.html#broadcast-variables

Create a broadcast variable. Type in:

broadcastVar = sc.broadcast([1,2,3])

To get the value, type in:

broadcastVar.value

## Accumulators

Accumulators are variables that can only be added through an associative operation. It is used to implement counters and sum efficiently in parallel. 
Spark natively supports numeric type accumulators and standard mutable collections. Programmers can extend these for new types. Only the driver can read the 
values of the accumulators. The workers can only invoke it to increment the value.

Create the accumulator variable. Type in:

accum = sc.accumulator(0)

Next parallelize an array of four integers and run it through a loop to add each integer value to the accumulator variable. Type in:

rdd = sc.parallelise([1, 2, 3, 4])
def f(x):
    global accum
    accum += x
    
Next, iterate through each element of the rdd and apply the function f on it:

rdd.foreach(f)

To get the current value of the accumulator variable, type in:

accum.value

You should get a value of 10.

This command can only be invoked on the driver side. The worker nodes can only increment the accumulator.

## Key-value pairs
You have already seen a bit about key-value pairs in the Joining RDD section.

Create a key-value pair of two characters. Type in:

pair = ('a', 'b')
To access the value of the first index use [0] and [1] method for the 2nd.

print(pair[0])
print(pair[1])


## Summary
Having completed this exercise, you should now be able to describe Spark’s primary data abstraction, work with Resilient Distributed Dataset (RDD) operations, 
and utilize shared variables and key-value pairs.

