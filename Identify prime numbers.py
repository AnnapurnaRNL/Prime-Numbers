####Check if a given number is prime or not#####
input_number = int(input("Enter a number:"))
prime_num = []
for i in range(1,input_number+1):
    if input_number%i == 0:
        prime_num.append(i)
print(prime_num)
if len(prime_num) == 2:
    print("Congratulations..! You have entered a Prime Number")
else:
    print("Input number is not a prime number..")

#Identify in input number is a prime numbers using list comphrension
input_number = int(input("Enter a number:"))
prime_num = [x for x in range(1,input_number+1) if input_number%x == 0]
if len(prime_num) == 2:
    print("You have entered a prime number..!")
else:
    print("Input number is not a prime number..")


####List prime numbers in a given range#####
a,b = 100,200
prime_numbers = []
for input_number in range(a,b):
    prime_num = []
    for i in range(1,input_number+1):
        if input_number%i == 0:
            prime_num.append(i)
#    print(prime_num)
    if len(prime_num) == 2:
        prime_numbers.append(i)
print("\nNumber of prime numbers between " + str(a) + " and " + str(b) + " are: " + str(len(prime_numbers)) + "\n")
print("Prime numbers in the given range are...\n" + str(prime_numbers))


####List prime numbers in a given range#####
##Give input numbers separated by a space
#Ex: 10 20
num1,num2 = input("Enter a number:").split()
a=int(num1)
b=int(num2)
prime_numbers = []
for input_number in range(a,b):
    prime_num = []
    for i in range(1,input_number+1):
        if input_number%i == 0:
            prime_num.append(i)
#    print(prime_num)
    if len(prime_num) == 2:
        prime_numbers.append(i)
print("\nNumber of prime numbers between " + str(a) + " and " + str(b) + " are: " + str(len(prime_numbers)) + "\n")
print("Prime numbers in the given range are...\n" + str(prime_numbers))


####List prime numbers in a given range#####
##Give input numbers separated by a space
#Ex: 10 20
num1,num2 = input("Enter a number:").split()
a=int(num1)
b=int(num2)
prime_numbers = []
for input_number in range(a,b):
    prime_num = [i for i in range(1,input_number+1) if input_number%i == 0]
    print(prime_num)
    if len(prime_num) == 2:
        prime_numbers.append(input_number)
print("\nNumber of prime numbers between " + str(a) + " and " + str(b) + " are: " + str(len(prime_numbers)) + "\n")
print("Prime numbers in the given range are...\n" + str(prime_numbers))

