def all_neg_ints_inclusive(nums):
    result = []
    for i in range(30, 88):
        if nums[i] < 0:
            result.append(nums[i])
    return result