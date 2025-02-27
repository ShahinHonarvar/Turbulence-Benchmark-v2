def all_neg_ints_inclusive(nums):
    neg_ints = []
    for i in range(27, 56):
        if nums[i] < 0:
            neg_ints.append(nums[i])
    return neg_ints