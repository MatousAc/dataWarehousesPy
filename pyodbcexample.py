#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 16:06:39 2022

@author: harveyalferez
"""

###Install the driver: https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver15
###https://pypi.org/project/pyodbc/
###https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Mac-OSX

import pyodbc 
import pandas as pd

server = 'localhost' 
database = 'university' 
username = 'sa' 
password = '362834aA_ABuZ' 

cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password+';TrustServerCertificate=yes;')
cursor = cnxn.cursor()

cursor.execute('SELECT * FROM instructor')

for i in cursor:
    print(i)
    
df = pd.read_sql_query('SELECT * FROM instructor', cnxn)

print(df)
print(type(df))