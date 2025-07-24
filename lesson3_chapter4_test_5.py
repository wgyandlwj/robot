temp = float(input("Enter a number: "))

if temp > 22:
    print("It's warm")
    print(f"new temp is {temp - 1}")

elif temp < 20:
    print("It's cold")
    print(f"new temp is {temp + 1}")

else:
    print("It's just right")
