                       # LEETCODE
# 1768. Merge Strings Alternately

# PROGRAM ===>

# def merge(word1,word2):
#     i = 0
#     result = []

#     while i < len(word1) and i < len(word2):
#         result.append(word1[i])
#         result.append(word2[i])
#         i += 1
    
#     if i < len(word1):
#         result.append(word1[i:])

#     if i < len(word2):
#         result.append(word2[i:])

#     return "".join(result)

# out = merge("abcd","xyz")
# print("After merging the output is :",out)

#Method 2

# word1 = input("Enter the first string :")
# word2 = input("Enter the second string :")

# i = 0
# result = []

# while i < len(word1) and i < len(word2):
#     result.append(word1[i])
#     result.append(word2[i])
#     i += 1

# if i < len(word1):
#     result.append(word1[i:])

# if i < len(word2):
#     result.append(word2[i:])

# newlis = "".join(result)
# print(newlis)
#________________________________________________________________________________________________________________________
# 1071. Greatest Common Divisor of Strings

# PROGRAM ==>

# class Solution:
#     def gcdOfStrings(self,str1, str2):
#         if str1 + str2 != str2 + str1:
#             return ""
        
#         a = len(str1)
#         b = len(str2)
        
#         while b != 0:
#             a, b = b, a % b
        
#         return str1[:a]
# obj = Solution()
# print(obj.gcdOfStrings("abab","ab"))
#_______________________________________________________________________________________________________________
# 1431. Kids With the Greatest Number of Candies

# PROGRAM ==>

# def Candies(candies,extra_candies):

#     result = []
#     max_candies = max(candies)
#     for candy in candies:
#         if candy + extra_candies >= max_candies:
#             result.append(True)
#         else:
#             result.append(False)
#     return result

# a = Candies([1,2,3,1,5],1)
# print(a)
#_______________________________________________________________________________________________________________________________
# 605. Can Place Flowers

#PROGRAM ==>

# class Solution:
#     def canPlaceFlowers(self, flowerbed:list[int], n :int):
#         if n == 0:
#             return True
        
#         for i in range (len(flowerbed)):
#             if flowerbed[i] == 0:
#                 left_empty = (i == 0) or (flowerbed[i - 1] == 0)
#                 right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
#                 if left_empty and right_empty:
#                     flowerbed[i] = 1
#                     n -= 1
#                     if n <= 0:
#                         return True
                        
#         return n <= 0
        
# obj = Solution()
# print(obj.canPlaceFlowers([1,0,0,0,1],1))

#____________________________________________________________________________________________________________________________
# 345. Reverse Vowels of a String

# PROGRAM ==>

# class Solution:
#     def reverseVowels(self, s: str):
#         s = list(s)
#         vowels = set("aeiouAEIOU")
#         left, right = 0, len(s) - 1

#         while left < right:
#             if s[left] not in vowels:
#                 left += 1
#             elif s[right] not in vowels:
#                 right -= 1
#             else:
#                 s[left], s[right] = s[right], s[left]
#                 left += 1
#                 right -= 1
#         return "".join(s)
    
# obj = Solution()
# print(obj.reverseVowels("IceCreAm"))
#___________________________________________________________________________________________________________________________
# 151. Reverse Words in a String

#Program ==>

# def reverseWords(s:str):
#     return " ".join(s.split()[::-1])

# print(reverseWords("Hello World"))

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         result = []
#         i = len(s) - 1

#         while i >= 0:
#             # Skip spaces
#             while i >= 0 and s[i] == ' ':
#                 i -= 1
            
#             if i < 0:
#                 break

#             # Mark end of word
#             j = i

#             # Move to start of word
#             while i >= 0 and s[i] != ' ':
#                 i -= 1

#             # Add word to result
#             result.append(s[i+1:j+1])

#         return ' '.join(result)
#___________________________________________________________________________________________________________________________
# 238. Product of Array Except Self

# PROGRAM ==>

# class Solution:
#     def productExceptSelf(self, nums :list[int]):
#         res = [1] * len(nums)

#         prefix = 1
#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix *= nums[i]
#         suffix = 1
#         for i in range(len(nums) - 1, -1, -1):
#             res[i] *= suffix
#             suffix *= nums[i]

#         return res
    
# obj = Solution()
# print(obj.productExceptSelf([1,2,3,4]))
#___________________________________________________________________________________________________________________________
# 334. Increasing Triplet Subsequence

# PROGRAM ==>

# class Solution:
#     def increasingTriplet(self, nums):
#         first = float('inf')
#         second = float('inf')

#         for num in nums:
#             if num <= first:
#                 first = num
#             elif num <= second:
#                 second = num
#             else:
#                 return True

#         return False
    
# obj = Solution()
# print(obj.increasingTriplet([5,4,3,2,1]))
#___________________________________________________________________________________________________________________________

# class Solution:
#     def compress(self, chars):
#         write = 0
#         read = 0

#         while read < len(chars):
#             char = chars[read]
#             count = 0

#             while read < len(chars) and chars[read] == char:
#                 read += 1
#                 count += 1

#             chars[write] = char
#             write += 1

#             if count > 1:
#                 for digit in str(count):
#                     chars[write] = digit
#                     write += 1

#         return write

#____________________________________________________________________________________________________________________________
# 283. Move Zeroes
#PROGRAM ==>

# class Solution:
#     def moveZeroes(self, nums):
#         j = 0
        
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 j += 1
#         return nums
    
# obj = Solution()
# print(obj.moveZeroes([0,1,0,3,12]))
#___________________________________________________________________________________________________________________________
# 392. Is Subsequence
#PROGRAM ==>

# class Solution:
#     def isSubsequence(self, s, t):
#         i = 0 
        
#         for j in range(len(t)):
#             if i < len(s) and s[i] == t[j]:
#                 i += 1
        
#         return i == len(s)
    
# obj = Solution()
# print(obj.isSubsequence("abc","ahbgdc"))
#___________________________________________________________________________________________________________________________
# 560. Subarray Sum Equals K
# PROGRAM ==>

# class Solution:
#     def subarraySum (self, nums : list[int], k : int):
#         res = 0
#         curSum = 0
#         prefixSumCount = {0: 1}

#         for n in nums :
#             curSum += n
#             diff = curSum - k

#             res += prefixSumCount.get(diff, 0)
#             prefixSumCount[curSum] = prefixSumCount.get(curSum, 0) + 1


#         return res
#____________________________________________________________________________________________________________________________
# 643. Maximum Average Subarray I
# PROGRAM ==>

# class Solution:
#     def findMaxAverage(self, nums: list[int], k: int) -> float:
#         window_sum = sum(nums[:k])
#         max_sum = window_sum

#         for i in range(k, len(nums)):
#             window_sum += nums[i]
#             window_sum -= nums[i - k]

#             max_sum = max(max_sum, window_sum)

#         return max_sum / k
#___________________________________________________________________________________________________________________________
# 1732. Find the Highest Altitude
#PROGRAM ==>

# class Solution:
#     def largestAltitude(self, gain: list[int]) -> int:
#         current_altitude = 0
#         max_altitude = 0

#         for g in gain:
#             current_altitude += g
#             max_altitude = max(max_altitude, current_altitude)

#         return max_altitude
#____________________________________________________________________________________________________________________________
# 724. Find Pivot Index
# PROGRAM ==>

# class Solution:
#     def pivotIndex(self, nums : list[int]) -> int:
#         left_sum  = 0
#         right_sum = sum(nums)

#         for i in range(len(nums)):
#             right_sum -= nums[i]
#             if left_sum == right_sum:
#                 return i
#             left_sum += nums[i]

#         return -1
#____________________________________________________________________________________________________________________________
# 2215. Find the Difference of Two Arrays
# PROGRAM ==>

# class Solution:
#     def findDifference(self, nums1 : list[int], nums2 : list[int]):
#         set1 = set(nums1)
#         set2 = set(nums2)

#         return [list(set1 - set2), list(set2 - set1)]

# obj = Solution()
# print(obj.findDifference([1,2,3], [2,4,6]))
#____________________________________________________________________________________________________________________________
# 1207. Unique Number of Occurrences
# PROGRAM ==>

# class Solution:
#     def unqiueOcuurences(self, arr :list[int]) -> bool:
#         count = {}

#         for num in arr:
#             count[num] = count.get(num, 0) + 1

#         frequencies = count.values()

#         return len(frequencies) == len(set(frequencies))
# obj = Solution()
# print(obj.unqiueOcuurences([1,2,2,3,3,3]))
#____________________________________________________________________________________________________________________________
# 933. Number of Recent Calls
# PROGRAM ==>

# from collections import deque

# class RecentCounter:

#     def __init__(self):
#         self.q = deque()

#     def ping(self, t: int) -> int:
#         self.q.append(t)

#         while self.q[0] < t - 3000:
#             self.q.popleft()

#         return len(self.q)
#____________________________________________________________________________________________________________________________
# 169. Majority Element

# PROGRAM ==>

# class Solution:
#     def majorityElement(self, nums):
#         candidate = None
#         count = 0

#         for num in nums:
#             if count == 0:
#                 candidate = num
            
#             if num == candidate:
#                 count += 1
#             else:
#                 count -= 1

#         return candidate

