def all_odd_ints_inclusive(nums):
    result = []
    for i in range(len(nums)):
        if i >= 68 and i <= 86 and (nums[i] % 2 != 0):
            result.append(nums[i])
    return result