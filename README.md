# PYSARK INSTALLATION AND AFTER INSTALLATION LOCAL-SQL-SERVER-CONNECT-VIA-PYTHON-
LOCAL SQL SERVER CONNECT VIA PYTHON 


Steps to install Apache spark 3.4.1 on windows 11

Download & install 7zip if not already available in your laptop
1) Download & install Python 3.11.9
2) Download & install Java JDK 17
3) Download Spark 3.4.3 - pre-built for Apache Hadpoop 3.4 & later
4) Extract the Spark downloaded files using 7 zip
5) Download Hadoop winutil from github
6) Create folder structure - C:\SPARK & C:\HADOOP\bin
7) Copy the downloaded Spark & Hadoop files into above folders respectively
8) Set the environment variables & path for Java, Spark & Hadoop
     1.)  HADOOP_HOME--->C:\hadoop
     2.)  JAVA_HOME----->C:\Program Files\Java\jdk-17
     3.)  PYSPARK_HOME-->C:\Users\<user name>\AppData\Local\Programs\Python\Python311\python.exe
     4.)  SPARK_HOME---->C:\spark\spark-3.4.3-bin-hadoop3
   under User path Variable
   %JAVA_HOME%\bin
   %HADOOP_HOME%\bin
   %SPARK_HOME%\bin
   %PYSPARK_HOME%\bin
10) Launch cmd from this path - C:\SPARK\bin - execute command spark-shell

Download links:
Apache Spark 3.4.3 - 
7 ZIP  - https://www.7-zip.org/download.html
Python 3.11.9- https://www.python.org/downloads/
JAVA 17  - https://www.oracle.com/in/java/technologies/downloads/#java17
Spark  3.4.3 - https://spark.apache.org/downloads.html
Hadoop winutils(hadoop-3.3.0) - https://github.com/NRIMOHAMMEDASIF/winutils-master


------------------------------------
# LOCAL-SQL-SERVER-CONNECT-VIA-PYTHON-

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
#Connection details
CONNECTOR_TYPE = "jdbc"
SQL_USERNAME = "XXXXXUSER"
SQL_PASSWORD = "XXXX"
SQL_DBNAME = "DB_NAME"
SQL_SERVERNAME = "SERVER_NAME"

#table name 
cc_table = "dbo.Asif_Practice_credit_card"
cust_table = "dbo.Asif_Practice_customer"

hr = "dbo.Payroll_Comparison_13_months"

if __name__ == "__main__":

    spark = SparkSession.builder \
        .appName("spark sql demo") \
        .getOrCreate()
     
    url = f"jdbc:sqlserver://{SQL_SERVERNAME};databaseName={SQL_DBNAME};"

    df_sales_header = spark.read \
        .format("jdbc") \
        .option("url", url) \
        .option("dbtable", hr) \
        .option("user", SQL_USERNAME) \
        .option("password", SQL_PASSWORD) \
        .load()
    
    df_sales_header.show(10,False)

    df_sales_header.printSchema()
