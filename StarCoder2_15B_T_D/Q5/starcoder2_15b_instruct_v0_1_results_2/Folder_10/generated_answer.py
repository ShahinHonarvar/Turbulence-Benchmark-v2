def all_neg_ints_inclusive(nums):
    output = []
    for i, num in enumerate(nums):
        if num < 0 and 25 <= i <= 59:
            output.append(num)
    return output