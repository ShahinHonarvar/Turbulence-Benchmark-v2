def all_neg_ints_inclusive(nums):
    neg_ints = []
    for i in range(len(nums)):
        if i >= 74 and i <= 95 and (nums[i] < 0):
            neg_ints.append(nums[i])
    return neg_ints