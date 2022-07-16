x = int(input("What's the number? "))

if x%4 == 0:
    print(f"{x} is a multiple of 4")
elif x%2 == 0:
    print(f"{x} is a even number")
else:
    print(f"{x} is a odd number")