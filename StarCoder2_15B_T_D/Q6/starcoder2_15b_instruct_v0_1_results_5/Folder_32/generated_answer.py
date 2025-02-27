def all_neg_ints_exclusive(nums):
    result = []
    for i, num in enumerate(nums):
        if num < 0 and 11 <= i < 76:
            result.append(num)
    return result