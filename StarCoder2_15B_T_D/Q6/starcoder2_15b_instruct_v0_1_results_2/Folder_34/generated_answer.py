def all_neg_ints_exclusive(nums):
    neg_ints = []
    for i in range(60, 200):
        num = nums[i]
        if num < 0:
            neg_ints.append(num)
    return neg_ints