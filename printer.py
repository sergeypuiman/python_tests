import os
import re
import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ . + ';DATABASE=' + TRN +';UID=' + test + ';PWD=' + test)
self.cursor = conn.cursor()
  
qualifier = re.sub(r'[-_]+', '', os.environ['BUILD_ID'])[0:12]

print ("---Master branch---")
print ("---Build# ", qualifier,"---")
print ("---END---")
