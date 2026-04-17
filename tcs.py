# This are the most asked TCS coding questions.






# Non-Repeating Element

#PROGRAM ==>

# def firstNonRepeating(arr):
#     freq  = {}
#     for num in arr:
#         freq[num] = freq.get(num, 0) + 1
#     for num in arr:
#         if frq[num] == 1:
#             return num 
#     return 0
#___________________________________________________________________



# def rotateLeft(arr, d):
#     n = len(arr)
#     d = d % n

#     def reverse(start, end):
#         while start < end:
#             arr[start], arr[end] = arr[end], arr[start]
#             start += 1
#             end -= 1

#     reverse(0, d - 1)
#     reverse(d, n - 1)
#     reverse(0, n - 1)

#     return arr
#___________________________________________________________________

# class Solution:
#     def subarraySum(self, nums : list[int], k : int):
#         res = 0
#         curSum = 0
#         prefixSumCount = {0: 1}

#         for n in nums :
#             curSum += n
#             diff = curSum - k

#             res += prefixSumCount.get(diff, 0)
#             prefixSumCount[curSum] = prefixSumCount.get(curSum, 0) + 1


#         return res



# Find the smallest element in an array

# def find_smallest(arr):
#     smallest = arr[0]

#     for num in arr:
#         if num < smallest:
#             smallest = num
    
#     return smallest


# def find_lagest(arr):
#     largest = arr[0]

#     for num in arr:
#         if num > largest:
#             largest = num 
#     return largest





# Second Smallest and Second Largest element in an array

# def find_second_elements(arr):
#     if len(arr) < 2:
#         return -1, -1

#     smallest = float('inf') 
#     second_smallest = float('inf')
#     largest = float('-inf')
#     second_largest = float('-inf')

#     for num in arr:
#         # Smallest & Second Smallest
#         if num < smallest:
#             second_smallest = smallest
#             smallest = num
#         elif smallest < num < second_smallest:
#             second_smallest = num

#         # Largest & Second Largest
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif largest > num > second_largest:
#             second_largest = num

#     # Edge case: if no second exists
#     if second_smallest == float('inf'):
#         second_smallest = -1
#     if second_largest == float('-inf'):
#         second_largest = -1

#     return second_smallest, second_largest


# # Example
# arr = [1, 2, 4, 7, 7, 5]
# print(find_second_elements(arr))  # Output: (2, 5)


# Reverse a given array

# def reverse_array(arr):
#     left = 0
#     right = len(arr) - 1

#     while left < right:
#         arr[left], arr[right] = arr[right], arr[left]
#         left += 1
#         right -= 1
#     return arr


# Count frequency of each element in an array

# def count_frequency(arr):
#     count = {}

#     for num in arr:
#         if num in count:
#             count[num] += 1
#         else:
#             count[num] = 1
#     return count

# Rearrange array in increasing-decreasing order


# def rearrange_array(arr):
#     n = len(arr)

#     arr.sort() 

#     mid = (n + 1) // 2 

#     first_half = arr[:mid]          
#     second_half = arr[mid:]         

#     second_half.reverse()

#     return first_half + second_half

# arr = [1, 2, 3, 4, 5, 6]
# print(rearrange_array(arr))

# Calculate Sum of the Elements of the Array

# def sum_of_array(arr):
#     total = 0
#     for num in arr:
#         total += num 
#     return total

# Average of all the elements in the array

# def average_of_array(arr):
#     if len (arr) == 0:
#         return 0
    
#     total = 0
#     for num in arr:
#         total += num
#     return total / len(arr)


# Find the median of the given array

# def find_median(arr):
#     n =  len(arr)

#     arr.sort()

#     if n % 2 == 1:
#         return arr[n // 2]
    
#     else:
#         mid1 = arr[n // 2 - 1]
#         mid2 = arr[n //2]
#         return(mid1 + mid2) / 2


# Remove duplicates from a sorted array

# def remove_duplicates(arr : list[int]) -> int:
#     if not arr:
#         return 0

#     i = 0  # points to last unique element

#     for j in range(1, len(arr)):
#         if arr[j] != arr[i]:
#             i += 1
#             arr[i] = arr[j]

#     return i + 1  # number of unique elements


# arr = [1,1,2,2,2,3,3]
# k = remove_duplicates(arr)


# Remove duplicates from unsorted array

# def remove_duplicates(arr):
#     seen = set()
#     result = []

#     for num in arr:
#         if num not in seen:
#             seen.add(num)
#             result.append(num)
#     return result


# Adding Element in an Array


# def insert_beggining(arr, element):
#     arr.insert(0, element)
#     return arr

# def insert_end(arr, element):
#     arr.append(element)
#     return arr

# def insert_at_position(arr, element, position):
#     if position < 0 or position > len(arr):
#         raise IndexError("Position out of bounds")
#     arr.insert(position, element)
#     return arr

# Find all repeating elements in an array


# def find_repeating(nums):
#     fre1 ={}

#     for num in nums:
#         fre1[num] = fre1.get(num, 0) + 1
    
#     return[num for num in fre1 if fre1[num] > 1]



# Find all non-repeating elements in an array

# def find_non_repeating(arr):
#     freq = {}

#     for num in arr:
#         freq[num] = freq.get(num, 0) + 1

#     result = [num for num, count in freq.items() if count == 1]

#     return result


# Find all Symmetric Pairs in the array of pairs

# def find_symmetric_pairs(pairs):
#     seen = {}
#     result = []

#     for a,b in pairs:
#         if b in seen and seen[b] == a:
#             result.append((a,b))
#         else:
#             seen[a] = b

#     return result


# Maximum product subarray in an array

def max_product_subarray(arr):
    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        num = arr[i]

        if num < 0:
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        result = max(result, max_prod)

    return result



# Replace each element of the array by its rank in the array

def replace_with_rank(arr):
    sorted_arr = sorted(arr)

    rank_map = {}
    rank = 1

    for num in sorted_arr:
        if num not in rank_map:   
            rank_map[num] = rank
            rank += 1

    result = [rank_map[num] for num in arr]

    return result


# Sorting elements of an array by frequency

def sort_by_frequency(arr):
    freq = {}

    # Step 1: Count frequency manually
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 2: Sort based on rules
    arr.sort(key=lambda x: (-freq[x], x))

    return arr


# Search an Element in an Array : Program CPP Java

def search_element(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1


# Check if array is subset of another array

def is_subset(arr1, arr2):
    set2 = set(arr2)

    for num in arr1:
        if num not in set2:
            return False
    return True


# Finding Equilibrium index in an array

def equilibrium_index(nums):
    left_sum = 0
    right_sum = sum(nums)

    for i in range(len(nums)):
        right_sum -= nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1


