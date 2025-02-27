def all_neg_ints_exclusive(nums):
    if not nums:
        return []
    neg_ints = []
    for i in range(13, 66):
        if nums[i] < 0:
            neg_ints.append(nums[i])
    return neg_ints