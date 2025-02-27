def all_neg_ints_inclusive(nums):
    output = []
    for i, num in enumerate(nums):
        if num < 0 and i >= 0 and (i <= 8):
            output.append(num)
    return output