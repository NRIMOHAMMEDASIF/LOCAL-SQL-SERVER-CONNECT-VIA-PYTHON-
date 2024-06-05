
from pyspark.sql import SparkSession

# CONNECTOR_TYPE = "com.microsoft.sqlserver.jdbc.spark"
CONNECTOR_TYPE = "jdbc"
SQL_USERNAME = "XXXXUSER"
SQL_PASSWORD = "XXXX"
SQL_DBNAME = "DB_NAME"
SQL_SERVERNAME = "SERVER_NAME" 


#table name 
cc_table = "dbo.Asif_Practice_credit_card"
cust_table = "dbo.Asif_Practice_customer"
hr = "dbo.Payroll_Comparison_13_months"

if __name__ == "__main__":

    spark = SparkSession.builder.appName("spark sql server").getOrCreate()

    # Set log level to WARN to reduce verbosity
    spark.sparkContext.setLogLevel("WARN")

    url = f"jdbc:sqlserver://{SQL_SERVERNAME};databaseName={SQL_DBNAME};"

    cc_table_df = spark.read\
            .format("jdbc")\
            .option("url",url)\
            .option("dbtable",cc_table)\
            .option("user",SQL_USERNAME)\
            .option("password",SQL_PASSWORD)\
            .load()
    

    
    cc_table_df.show(truncate=False)