def all_pos_ints_inclusive(nums):
    res = []
    for i in range(62, 64):
        if nums[i] > 0:
            res.append(nums[i])
    return res