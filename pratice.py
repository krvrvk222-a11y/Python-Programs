#Find the second largest element in the list
#Method1

# lst = list(map(int,input("Enter the numbers :").split(",")))
# lst.sort()
# print(lst)
# print("The second largest element in the list is :",lst[-2])

#Method2

# mylist = list(map(int,input("Enter the number :").split(",")))
# newlist = set(mylist)
# print(newlist)
# newlist.remove(max(newlist))
# print(newlist)
# print(max(newlist))
#_________________________________________________________________________________________
#Check if two strings are anagrams

# #Method 1

# s1 = input("Enter first string :").replace(" ","").lower()
# s2 = input("Enter second string :").replace(" ","").lower()
# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not anagram")
# print(sorted(s1))

#Method2
# from collections import Counter
# s1 = input("Enter first string :").replace(" ","").lower()
# s2 = input("Enter second string :").replace(" ","").lower()
# if Counter(s1) == Counter(s2):
#     print("Anagram")
# else:
#     print("Not anagram")
# print(sorted(s1))

#___________________________________________________________________________________
#Find missing number in 1..n

# nums = list(map(int,input("Enter the numbers :").split(",")))
# n = len(nums)+1
# excepted_sum = n * (n + 1) //  2
# actual_sum = sum(nums)
# print("Missing number is :",excepted_sum - actual_sum)
#______________________________________________________________________
#Moves all zeros to the end of the list

# nums = [0,2,0,1,3,0,4]
# result = []
# zero_count = 0
# for n in nums:
#     if n == 0:
#         zero_count += 1
#     else:
#         result.append(n)
# for i in range(zero_count):
#     result.append(0)
# print(result)
#___________________________________________________________________
# Merge two sorted lists into one sorted list

# a = [1,3,5,7]
# b = [2,4,6]

# i = 0
# j = 0
# merged =[]

# while i < len(a) and j < len(b):
#     if a[i] <= b [j]:
#         merged.append(a[i])
#         i+=1
#     else:
#         merged.append(b[j])
#         j+=1
# while i < len(a):
#     merged.append(a[i])
#     i+=1
# while j < len(b):
#     merged.append(b[j])
#     j+=1

# print(merged)
#________________________________________________________________________________
#Longest word in the sentence 

# sentence = "I love programming in python"

# words = sentence.split()
# longest = ""
# for w in words:
#     if len(w) > len(longest):
#         longest = w

# print("longest word :",longest)
# print("Length",len(longest))
#_________________________________________________________________________________

# from collections import deque

# class Solution:
#     def levelOrder(self, root):
#         if not root:
#             return []
        
#         result = []
#         queue = deque([root])
        
#         while queue:
#             level_size = len(queue)
#             level = []
            
#             for _ in range(level_size):
#                 node = queue.popleft()
#                 level.append(node.val)
                
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
            
#             result.append(level)
        
#         return result

class Solution:

