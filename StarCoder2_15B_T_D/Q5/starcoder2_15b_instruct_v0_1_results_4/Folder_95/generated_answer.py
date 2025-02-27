def all_neg_ints_inclusive(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] < 0 and 82 <= i <= 86:
            result.append(nums[i])
    return result