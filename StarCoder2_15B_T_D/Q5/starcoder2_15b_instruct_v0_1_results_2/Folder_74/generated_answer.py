def all_neg_ints_inclusive(nums):
    result = []
    for i in range(17, 79):
        if nums[i] < 0:
            result.append(nums[i])
    return result