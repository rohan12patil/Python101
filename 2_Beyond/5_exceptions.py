

# try:
#     x  = 10/0
# except:
#     print("That didn't work")

# Catch exceptions

try: 
    answer = input("What should I divide 10 by ?")
    num = int(answer)
    print(10/num)

except ZeroDivisionError as e:
    print("Cannot divide by zero")
except ValueError as e:
    print("You didn't give me a valid number")
    print(e)
finally:
    print("Finally always works")