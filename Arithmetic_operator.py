# Writeb a python program to do arithmetical operations and division.
num_1 = float(input("Enter the first addition number: "))
num_2 = float(input("Enter the second addition number: "))
num_3 = float(input("Enter the first division number: "))
num_4 = float(input("Enter the second division number: "))
sum_result = num_1 + num_2
if num_4 ==0:
    print("error : Division by Zero is not allowed")
else:
    div_result = num_3 / num_4
    print(f"divison: {num_3} / {num_4} = {div_result}")
print(f"sum: {num_1}+{num_2} = {sum_result}")