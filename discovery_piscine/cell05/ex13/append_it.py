import sys
import re
count = 0
if len(sys.argv) < 2:
    print("none")
else:
    for i in range(1,len(sys.argv)):
        if re.search(r"ism$", sys.argv[i]):
            continue
        else:
            print(sys.argv[i]+"ism")