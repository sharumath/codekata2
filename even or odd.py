num = int(input("Enter a number:"))
flag = num % 2
if flag > 0:
   print("given number is odd")
elif flag == 0:
   print("given number is even")
else:
   print("given input is invalid")
