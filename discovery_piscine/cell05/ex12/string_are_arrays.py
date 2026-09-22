import sys
count = 0
if len(sys.argv) != 2:
    print("none")
else:
    for i in sys.argv[1]:
        if i == "z":
            print(i,end="")
            count+=1
    if count > 0:
        print()
if count == 0:
    print("none")

        