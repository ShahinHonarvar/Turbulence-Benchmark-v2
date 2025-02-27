def all_neg_ints_exclusive(nums):
    neg_ints = []
    for i in range(len(nums)):
        if nums[i] < 0 and 90 < i < 200:
            neg_ints.append(nums[i])
    return neg_ints