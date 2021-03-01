
# class Solution(object):
#     def sortArrayByParity(self, unsorted):
#       i = 0
#       j =0
#       while j < len(unsorted):
#          if unsorted[j]%2==1:
#             unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
#             i+=1
#          j+=1
#       return unsorted
# ob1 = Solution()
# print(ob1.sortArrayByParity([5, 2, 7, 8, -2, 25, 25]))
def meanderingArray(unsorted):
    nums = len(unsorted)
    unsorted.sort()

    empty_array = [0] * (nums + 1)

    array_index = 0

    i = 0
    j = nums - 1

    while (i <= nums // 2 or j > nums // 2):
        #print("{} {} {}".format(i, j, array_index))
        empty_array[array_index] = unsorted[j]
        array_index = array_index + 1
        if array_index < len(empty_array):
            empty_array[array_index] = unsorted[i]
        array_index = array_index + 1
        i = i + 1
        j = j - 1
    for i in range(0, nums):
        unsorted[i] = empty_array[i]
    return unsorted


print(meanderingArray([5, 2, 7, 8, -2, 25, 25]))
