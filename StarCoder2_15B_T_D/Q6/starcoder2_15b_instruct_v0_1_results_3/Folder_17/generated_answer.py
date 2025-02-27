def all_neg_ints_exclusive(nums):
    neg_ints = []
    for i in range(len(nums)):
        if i >= 62 and i < 96 and (nums[i] < 0):
            neg_ints.append(nums[i])
    return neg_ints