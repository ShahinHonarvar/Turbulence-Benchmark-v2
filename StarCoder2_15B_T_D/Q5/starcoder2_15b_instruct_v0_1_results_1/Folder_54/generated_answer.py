def all_neg_ints_inclusive(nums):
    res = []
    for i in range(len(nums)):
        if nums[i] < 0 and 34 <= i <= 55:
            res.append(nums[i])
    return res