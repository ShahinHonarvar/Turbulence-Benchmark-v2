def all_neg_ints_inclusive(nums):
    neg_nums = []
    for i in range(209, 557):
        if nums[i] < 0:
            neg_nums.append(nums[i])
    return neg_nums