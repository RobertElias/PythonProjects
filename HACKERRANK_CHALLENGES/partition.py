# def partitionArray(k, numbers):
#     # Write your code here
#     nums = numbers
#     if not nums and k == 1:
#         return True

#         if k > len(nums) % len(nums):
#             return False
#     count = {i: nums.count(i) for i in nums}

#     if len(nums) // k < max(count.values()):
#         return False
#     # Then call the return
#     return True


# print(partitionArray([1, 2, 3, 4], 2))
# print(partitionArray([1, 2, 2, 4], 3))
# print(partitionArray([3, 5, 3, 2], 2))
# print(partitionArray([4, 8, 8, 8, 6, 4], 3))


def partitionArray(numbers, k):
       # if array exists and length is 1
   if not numbers and k == 1:
       return True
   # if partition size is bigger return False
   if k > len(numbers) or len(numbers) % len(numbers):
       return False
   #counting number of occurences of each number
   count = {i: numbers.count(i) for i in numbers}
   # if max repeated value in array
   # is greater than number of values in each partion
   # return false
   if len(numbers)// k < max(count.values()):
       return "No"
   #return True
   return "Yes"
   

print(partitionArray([1, 2, 3, 4], 2))
print(partitionArray([1, 2, 2, 4], 3))
print(partitionArray([3, 5, 3, 2], 2))
print(partitionArray([4, 8, 8, 8, 6, 4], 3))
