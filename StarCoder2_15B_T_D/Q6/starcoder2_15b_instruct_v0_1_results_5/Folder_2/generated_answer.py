def all_neg_ints_exclusive(nums):
    result = []
    for i in range(36, 52):
        if nums[i] < 0:
            result.append(nums[i])
    return result