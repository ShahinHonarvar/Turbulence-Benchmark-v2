def all_neg_ints_exclusive(nums):
    result = []
    for num in nums:
        if num < 0:
            result.append(num)
    if len(result) > 0:
        return result
    else:
        return []