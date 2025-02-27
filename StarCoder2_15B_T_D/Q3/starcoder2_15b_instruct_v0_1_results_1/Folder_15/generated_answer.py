def all_pos_ints_inclusive(nums):
    pos_ints = []
    for i, num in enumerate(nums):
        if num > 0 and i >= 0 and (i <= 3):
            pos_ints.append(num)
    return pos_ints