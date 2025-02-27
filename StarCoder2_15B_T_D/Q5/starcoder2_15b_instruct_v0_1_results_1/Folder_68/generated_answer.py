def all_neg_ints_inclusive(nums):
    result = []
    for i, num in enumerate(nums):
        if num < 0 and i >= 0 and (i <= 8):
            result.append(num)
    return result