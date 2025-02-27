def all_neg_ints_inclusive(nums):
    result = []
    for i in range(len(nums)):
        if i >= 6 and i <= 8 and (nums[i] < 0):
            result.append(nums[i])
    return result