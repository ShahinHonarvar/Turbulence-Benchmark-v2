def all_neg_ints_exclusive(nums):
    result = []
    for i in range(len(nums)):
        if i >= 20 and i < 200 and (nums[i] < 0):
            result.append(nums[i])
    return result