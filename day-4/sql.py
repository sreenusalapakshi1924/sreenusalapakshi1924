import pyodbc
server='HYDTRNG10\SQLEXPRESS'
database='msdb'
username='sa'
password='admin@123'
cxcn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


mycursor=cxcn.cursor()
res=mycursor.execute("select * from emp")
myrecs=res.fetchall();
print(myrecs)