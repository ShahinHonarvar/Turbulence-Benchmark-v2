def all_neg_ints_exclusive(nums):
    result = []
    for i in range(len(nums)):
        if i >= 0 and i < 9:
            if nums[i] < 0:
                result.append(nums[i])
    return result