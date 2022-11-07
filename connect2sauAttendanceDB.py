import pyodbc 
cnxn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:matousacserver.database.windows.net,1433;Database=attendanceDB;Uid={matoush@southern.edu};Pwd={while S in range(5):};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;Authentication=ActiveDirectoryPassword')

cursor = cnxn.cursor()	
cursor.execute("select * from room") 
row = cursor.fetchone() 
while row:
  print (row) 
  row = cursor.fetchone()