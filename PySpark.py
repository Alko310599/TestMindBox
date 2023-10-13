from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, explode

# Создаем сессию Spark
spark = SparkSession.builder.appName("example").getOrCreate()

# Создаем DataFrame с данными о продуктах
product_data = [(1, "Apple"), (2, "Banana"), (3, "Orange"), (4, "Сheese"), (5, "Milk"), (6, "Bread"), (7, "Tea"), (8, "Grapes Juice"), (9, "Pasta"), (10, "Turkey meat")]
product_columns = ["ProductID", "ProductName"]
products_df = spark.createDataFrame(product_data, product_columns)

products_df.show()

# Создаем DataFrame с данными о категориях
category_data = [(1, "Fruit"), (2, "Dairy products"), (3, "Bakery"), (4, "Beverages"), (5, "Juices"), (6, "Meat"), (7, "Grocery") ]

category_columns = ["CategoryID", "CategoryName"]
categories_df = spark.createDataFrame(category_data, category_columns)

# Создаем DataFrame со связями о категориях и продуктах
connection_data = [(1,1), (2,1), (3,1), (4,2), (5,2), (6,3), (7,4), (7,7), (8,4), (8,5), (9,7)]
connection_columns = ["ProductID", "CategoryID"]
connection_df = spark.createDataFrame(connection_data, connection_columns)

result_df = products_df.join(connection_df, "ProductID", "left").join(categories_df, "CategoryID", "left")
result_df = result_df.select("ProductName","CategoryName")

result_df.show()
