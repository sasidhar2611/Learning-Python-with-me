'''Question 1'''

'''My version'''
# l = [-45, 67, 12, -68, -69, 34, 0]

# for i in range(len(l)):
#     if l[i] > 0:
#         print(f"{l[i]} is a positive number")
#     elif l[i] < 0:
#         print(f"{l[i]} is a negative number")
#     else:
#         print("0 is neither negative nor positive")

'''YT version'''

# l = [-45, 67, 12, -68, -69, 34, 0]

# print("Positive Elemnts")
# for i in l:
#     if i >= 0:
#         print(i)

# print("Negative elemnts")
# for i in l:
#     if i < 0:
#         print(i)


'''Question 2'''

# l = [1,2,3,4,5,6,7,8,9,10]

# sum = 0
# count = 0
# for i in range(len(l)):
#     sum += l[i]
#     count += 1
# mean = sum/count

# print(f"The mean of the elemnts is {mean}")

'''YT approach'''

# l = [1,2,3,4,5,6,7,8,9,10]

# sum = 0
# for i in l:
#     sum += i
    
# mean = sum/len(l)

# print(f"The mean of the elemnts is {mean}")

'''Question 3'''

# l = [31,543,765,1234567,3,5467,20,86097]
# greatest = l[0]
# index = 0
# for i in range(len(l)):
#     if greatest < l[i]:
#         greatest = l[i]
#         index = i

# print(f"{greatest} is the greatest number at index = {index}")

'''Question 4'''

# l = [31,543,765,1234567,3,5467,20,86097]
# greatest = l[0]
# second = l[0]
# index1 = 0
# index2 = 0

# for i in range(len(l)):
#     if l[i] > greatest:
#         second = greatest
#         index2 = index1
#         greatest = l[i]
#         index1 = i
#     elif l[i] > second and l[i] != greatest:
#         second = l[i]
#         index2 = i

# print(f"The greatest number is {greatest} at {index1} ans the second greatest number is {second} at index {index2}")

'''Question 5'''

# l = [1,2,3,4]

# for i in range(len(l)-1):
#     if l[i] < l[i+1]:
#         continue
#     else:
#         print("Your list is not sorted")
#         break
# else:
#     print("Your list is sorted")

