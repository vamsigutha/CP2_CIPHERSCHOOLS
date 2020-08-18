# link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if (n < 2):
            return n
        idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[idx] = nums[i]
                idx += 1
        return idx


"""
assign idx as 1
start loop from second element until the end of the aray
check if current element is not equal to previous element then do
-> set idx element as current element and increment idx
at some time we remove duplicates before idx so return idx

0,1,1,2,3,3 -> idx = 1, i=1
0,1,1,2,3,3 -> idx = 2, i=2
0,1,1,2,3,3 -> idx = 2, i=3 
0,1,2,2,3,3 -> idx = 3, i=4
0,1,2,3,3,3 -> idx = 4, i=5

since i reached end of an array we return idx that is length of non-duplicates array

"""
