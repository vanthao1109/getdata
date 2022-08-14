#read data csv
import pandas as pd
import io
import requests
import mysql.connector as msql
from mysql.connector import Error
from numpy import sin
from numpy import sqrt
from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot
import os.path
url="https://storage.googleapis.com/kagglesdsdata/datasets/205965/451952/supermarket_sales%20-%20Sheet1.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20220814%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220814T031358Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=50f5af29344effd8efdd0017f6a9cc5f34f1314618d032da4ed34c5374187ab315453ae15b0a539a595c972469c2135bc1da0a5a202f7918662ac762a2d72241d66d7b396c9f4f73f9804e8fda9afa81f02361131f14aa75dedc3e560b08707a7eadcf701386f2144fc8267af7093213efa77a7bc2ad7b5dfb1874a6e805e601f151697ff308fd18b6c9fc00811324fb9dbef2a61d93a3e2816da55524330ad0c630ac25523932b8b2fe8896610e937ccdcf33c3df4e8b43bc43204b0260fa1a5bf243471c1421d9ed42e5cfc169a650c298db3c22e8921ece034a2d9f2965ff537854939da05c81165ecc94c51f45cee50dba016281fffc2e3f8a6bf6be1a63"
s=requests.get(url).content
empdata=pd.read_csv(io.StringIO(s.decode('utf-8')))
empdata.head()

# define the true objective function
def objective(x, a, b, c, d):
	return a * sin(b - x) + c * x**2 + d
data=empdata.values
x,y= data[:, 6], data[:, 8]
# curve fit
popt, _ = curve_fit(objective, x, y)
# summarize the parameter values
a, b, c, d = popt

# plot input vs output
pyplot.scatter(x, y)
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
# calculate the output for the range
y_line = objective(x_line, a, b, c, d)
# create a line plot for the mapping function
pyplot.plot(x_line, y_line, '--', color='red')
if os.path.exists(r'C:\Users\THAO\OneDrive\Desktop\New folder\getdata\data_site\image\fit_graph.jpg'):
    os.remove(r'C:\Users\THAO\OneDrive\Desktop\New folder\getdata\data_site\image\fit_graph.jpg')
pyplot.savefig(r'C:\Users\THAO\OneDrive\Desktop\New folder\getdata\data_site\image\fit_graph.jpg')
pyplot.show()


 
#create database
try:
    conn = msql.connect(host='localhost', user='root',  
                        password='vanthao1109')#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS customer_ins")
        #print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)
    
#create table
try:
    conn = msql.connect(host='localhost', database='customer_ins', user='root', password='vanthao1109')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS customer_data;')
        print('Creating table....')
# in the below line please pass the create table statement which you want to create
        cursor.execute("CREATE TABLE customer_data(Invoice_ID varchar(255),Branch varchar(30),City varchar(50),Customer varchar(20),Sex varchar(20),Product varchar(100),Price decimal,Quantity int,Tax decimal,Total_Price decimal,Date varchar(50),Time varchar(20), Payment varchar(30), Cogs decimal, Gross_Margin_Percentage decimal, Gross_Income decimal, Rating decimal)")
        print("Table is created....")
        #loop through the data frame
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO customer_ins.customer_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))

            
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
        cursor.execute("ALTER TABLE customer_data ADD COLUMN id INT AUTO_INCREMENT NOT NULL PRIMARY KEY")
        conn.commit()
        
        print("Record inserted")
except Error as e:
            print("Error while connecting to MySQL", e)
    
    
    
    
    
    
    
    