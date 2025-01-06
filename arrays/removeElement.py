n = [3, 2, 2, 3]
v = 2

def removeElement(nums, val):
    k = 0
    for i in range(1, len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k+=1
    return k


print(removeElement(n, v))
