def all_neg_ints_exclusive(nums):
    output = []
    for i, num in enumerate(nums):
        if num < 0 and 20 < i < 36:
            output.append(num)
    return output