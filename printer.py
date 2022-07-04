import os
import re
import pyodbc

conn = pyodbc.connect(r'Driver=FreeTDS;Server=.\SQLEXPRESS;Database=TRN;Trusted_Connection=yes;')
self.cursor = conn.cursor()
  
qualifier = re.sub(r'[-_]+', '', os.environ['BUILD_ID'])[0:12]

print ("---Master branch---")
print ("---Build# ", qualifier,"---")
print ("---END---")
