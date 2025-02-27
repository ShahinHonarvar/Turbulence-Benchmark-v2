def all_neg_ints_inclusive(nums):
    result = []
    for i in range(len(nums)):
        if i >= 30 and i <= 48 and (nums[i] < 0):
            result.append(nums[i])
    return result