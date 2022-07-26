def twoSum(nums,target):
   # count=1
    for i in range(len(nums)-1):
        a=nums[i]
        for j in range(i+1,len(nums)):
            b=nums[j]
            print(j,[a,b])
            
            if a+b == target:
                return [i,j]
           

#twoSum([3,2,4],6)

print(twoSum([2,7,11,15],9))