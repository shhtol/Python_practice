import random

#------Checking if number is even

number = int(input("Enter a number: "))

if (number % 2) == 0:  
   print("Even")  
else:  
   print("Odd")


#------Sum of digits

num = random.randint(100, 1000)
num_sum = 0
n = 0
print("Number is {}".format(num))
while num > 0:
    n = num%10
    num_sum += n
    num //= 10
print("Sum is {}".format(num_sum))

#------Finding min and max values in random numbers without lists or arrays
rand_num = 0
minimum = 100
maximum = 0
for i in range(10):
    rand_num = random.randint(1, 100)
    if rand_num > maximum:
        maximum = rand_num
    if rand_num < minimum:
        minimum = rand_num
    print(rand_num)

print("Max is {}".format(maximum))
print("Min is {}".format(minimum))

#------All words in one string

strng = ""
for i in range(5):
    word = input("Enter your word: ")
    strng += word + ' '
print(strng)

































    
        
