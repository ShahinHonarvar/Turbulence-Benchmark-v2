def all_pos_ints_inclusive(nums):
    pos_ints = []
    for i in range(56, 83):
        if nums[i] > 0:
            pos_ints.append(nums[i])
    return pos_ints