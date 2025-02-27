def all_pos_ints_exclusive(nums):
    pos_ints = []
    for i in range(len(nums)):
        if i >= 0 and i < 7 and (nums[i] > 0):
            pos_ints.append(nums[i])
    return pos_ints