import os
import re
import pyodbc

conn = pyodbc.connect('DRIVER=FreeTDS;SERVER=localhost;PORT=1433;DATABASE=TRN;UID=test;PWD=test;')
self.cursor = conn.cursor()
  
qualifier = re.sub(r'[-_]+', '', os.environ['BUILD_ID'])[0:12]

print ("---Master branch---")
print ("---Build# ", qualifier,"---")
print ("---END---")
