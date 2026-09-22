i = 0
j = 0
while i <= 10:
    print(f"Table de {i}: ",end="")
    while j <= 10:
        print(f"{j*i} ",end="")
        j+=1
    print()
    i+=1
    j=0