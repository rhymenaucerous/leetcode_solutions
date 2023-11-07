class Solution:
    def twoSum(self, nums, target: int):
        seen = {}
        nums_len = len(nums)
        for index in range(nums_len):
            seen[nums[index]] = index
        
        for index in range(nums_len):
            try:
                diff = target - nums[index]

                res_index = seen[diff]

                if res_index == index:
                    continue
                    
                return [res_index, index]
            except KeyError:
                continue

        return [0, 0]
    
# Supports understanding that hash tables should be used when possible

