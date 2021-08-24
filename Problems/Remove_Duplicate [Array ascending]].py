class Solution:

        def removeDuplicates(self, nums):

          i = 0
          while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
          return len(nums),nums

nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
print(s.removeDuplicates(nums))

# def removeDuplicates(self, nums):
    #   max = None
    #   i = 0
    #   while nums[i:i+1] != []:

    #     print(i,max,"\n",nums)
    #     if max == None:
    #       max = nums[i]
    #     elif max < nums[i]:
    #       max = nums[i]
    #     elif max == nums[i]:
    #       count = 0 
    #       n = 1
    #       while nums[i] == nums[i+n]:
    #         print("hi")
    #         count += 1
    #         n += 1
    #       nums = nums[:i] + nums[(i+count):]
    #     i += 1
    #   return len(nums),nums
