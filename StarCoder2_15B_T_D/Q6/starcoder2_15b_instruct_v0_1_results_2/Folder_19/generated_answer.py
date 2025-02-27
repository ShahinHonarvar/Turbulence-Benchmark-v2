def all_neg_ints_exclusive(nums):
    result = []
    for i, num in enumerate(nums):
        if 2 <= i < 5 and num < 0:
            result.append(num)
    return result