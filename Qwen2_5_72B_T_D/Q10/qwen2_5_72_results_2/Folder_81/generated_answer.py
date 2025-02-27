def all_odd_ints_exclusive(nums):
    result = []
    for i in range(10, 12):
        if i < len(nums) and nums[i] % 2 != 0:
            result.append(nums[i])
    return result