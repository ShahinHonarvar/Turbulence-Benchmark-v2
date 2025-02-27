def all_neg_ints_inclusive(nums):
    result = []
    for num in nums[29:94]:
        if num < 0:
            result.append(num)
    return result