def all_neg_ints_inclusive(nums):
    neg_ints = []
    for i, num in enumerate(nums):
        if num < 0 and 22 <= i <= 50:
            neg_ints.append(num)
    return neg_ints