print ("~~~~~~~~~~~ Mini Calculator~~~~~~~~~~~~~")

num1 = float(input("Enter First Number here: "))
num2 = float(input("Enter Second number here:"))

print("press 1 for Addition \npress 2 for Substraction \npress 3 for Multiplication \npress 4 for Division")

choice = int(input("Enter your Choice:"))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
else:
    print("Invalid choice")