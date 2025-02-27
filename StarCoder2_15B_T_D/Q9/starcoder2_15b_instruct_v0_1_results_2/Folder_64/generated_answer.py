def all_odd_ints_inclusive(nums):
    res = []
    for i in range(len(nums)):
        if i % 2 == 1 and 0 <= i <= 4:
            res.append(nums[i])
    return res