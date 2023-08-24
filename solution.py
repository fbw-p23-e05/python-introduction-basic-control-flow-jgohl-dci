# # Task 1
# i = 0

# while i < 3:
#     number = int(input('Enter number: '))
#     i += 1
#     number = number & 1

#     if number == 0:
#         print('Even number')
#     else:
#         print('Odd number')



# # Task 2
# output = 0
# i = 0

# while i < 3:
#     number = int(input('Enter number: '))
#     i += 1
#     output += number

# print('Sum of the numbers: ', output)



# Task 3
# i = 0
# output = []

# while i < 5:
#     number = int(input('Enter number: '))
#     i += 1
#     output.append(number)

# print('Highest number: ', max(output))



# Task 4
number = int(input('Enter number: '))

for i in range(2, number + 1):
    if number % i == 0:
        print(i)
