import os
import re
qualifier = re.sub(r'[-_]+', '', os.environ['BUILD_ID'])[0:12]

print ("---Master branch---")
print ("---Build# ", qualifier,"---")
