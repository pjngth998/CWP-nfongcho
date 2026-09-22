import sys
count = 0
if len(sys.argv) != 3:
    print("none")
else:
    lst = list(range(int(sys.argv[1]),int(sys.argv[2])+1))
    print(lst)