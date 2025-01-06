def twoSum(self, nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

    return []

