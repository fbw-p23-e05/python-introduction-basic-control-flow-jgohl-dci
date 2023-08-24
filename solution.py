# # Task 1
i = 0

while i < 3:
    number = int(input('Enter number: '))
    i += 1
    number = number & 1

    if number == 0:
        print('Even number')
    else:
        print('Odd number')



# # Task 2
output = 0
i = 0

while i < 3:
    number = int(input('Enter number: '))
    i += 1
    output += number

print('Sum of the numbers: ', output)



# Task 3
i = 0
output = []

while i < 5:
    number = int(input('Enter number: '))
    i += 1
    output.append(number)

print('Highest number: ', max(output))



# Task 4
number = int(input('Enter number: '))

for i in range(2, number + 1):
    if number % i == 0:
        print(i)



# Task 5
number = int(input('Enter number: '))

if number % 3 == 0 and number % 2 == 0:
    print(number, 'is even and divisible by 3')



# Task 6
number = int(input('Enter number: '))

if number >= 0 and number % 7 == 0 and number % 2 != 0:
    print(number, 'is positive, odd and divisible by 7')
else:
    print('The number is not positive, divisible by 7 or even')