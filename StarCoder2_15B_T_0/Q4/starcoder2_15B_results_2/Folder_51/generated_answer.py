def all_pos_ints_exclusive(nums):
    pos_ints = []
    for i, num in enumerate(nums):
        if num > 0 and 6 <= i < 9:
            pos_ints.append(num)
    return pos_ints