# Given an array of integers nums and an integer target, return 
# indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
    # Input: nums = [2,7,11,15], target = 9
    # Output: [0,1]
    # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

# Example 2:
    # Input: nums = [3,2,4], target = 6
    # Output: [1,2]

    # Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

def twosum(nums,target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
                     
print(twosum([2,7,11,15],9))











# def twoSum(nums,target):
#    # count=1
#     for i in range(len(nums)-1):
#         a=nums[i]
#         for j in range(i+1,len(nums)):
#             b=nums[j]
#             print(j,[a,b])
            
#             if a+b == target:
#                 return [i,j]
           

# #twoSum([3,2,4],6)

# print(twoSum([2,7,11,15],9))