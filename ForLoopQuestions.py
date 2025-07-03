'''Question 1'''

# n = int(input("Give me a number: "))

# for i in range(0,n,1):
#     print("Hello World!")


'''Question 2'''

# N = int(input("Give me a number: "))

# for i in range(1,N+1,1):
#     print(i)

'''Question 3'''
# N = int(input("Give me a number: "))

# for i in range(N,0,-1):
#     print(i)


'''Question 4'''

# n = int(input("Which table you want to print: "))
# m = int(input("Untill which multiple: "))

# for i in range(n, (n*m)+1, n):
#     print(f"{n} x {int(i/n)} = {i}")


'''Question 4'''

# N = int(input("Give me a number: "))
# sum = 0
# for i in range(1,N+1,1):
#     sum += i

# print(f"The sum is {sum}")

'''Question 5'''

# N = int(input("Give me a number: "))

# product = 1

# for i in range(1,N+1,1):
#     product *= i

# print(f"The factorial is {product}")

'''Question 6'''

# N = int(input("Give me a number: "))

# sum_even = 0
# sum_odd = 0

# for i in range(1,N+1,1):
#     if i % 2 == 0:
#         sum_even += i
#     else:
#         sum_odd += i

# print(f"The even number sum is {sum_even}")
# print(f"The odd number sum is {sum_odd}")

'''Question 7'''

# N = int(input("Give me a number: "))

# for i in range(1,N+1,1):
#     if N % i == 0:
#         print(i)

'''Question 8'''

# N = int(input("Give me a number: "))

# sum = 0
# for i in range(1,N,1):
#     if N % i == 0:
#         sum += i

# if sum == N:
#     print(f"The number {N} is a perfect number")
# else:
#     print(f"The number {N} is not a perfect number")

'''Question 9'''

# n = int(input("Give me a number: "))
# count = 0
# for i in range(1, n+1,1):
#     if n % i == 0:
#         count = count + 1

# if count == 2:
#     print("It is a Prime number")
# else:
#     print("It is a composite number")

'''Question 10'''

# a = "SHERYIANS"
# b = ""

# for i in range(len(a)-1, -1, -1):
#     b = b + a[i]

# print(b)

'''Question 11'''

# a = input("Give me a String: ")
# b = ""

# for i in range(len(a)-1, -1, -1):
#     b = b + a[i]

# if b == a:
#     print(f"Your string {a} is a palindrome")
# else:
#     print(f"Your string {a} is not a palindrome")

'''Question 12'''
# a = input("Give me a String: ")
# count_char = 0
# count_digits = 0
# count_symbol = 0

# for i in a:
#     if i.isdigit():
#         count_digits +=1
#     elif i.isalpha():
#         count_char += 1
#     else:
#         count_symbol += 1    

# print(f"Digits = {count_digits}")
# print(f"Characters = {count_char}")
# print(f"Symbols = {count_symbol}")