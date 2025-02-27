def all_neg_ints_inclusive(nums):
    result = []
    for i, num in enumerate(nums):
        if num < 0 and 3 <= i <= 5:
            result.append(num)
    return result