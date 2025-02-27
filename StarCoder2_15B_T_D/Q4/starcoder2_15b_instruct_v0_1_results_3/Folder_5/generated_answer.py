def all_pos_ints_exclusive(nums):
    pos_ints = []
    for i, num in enumerate(nums):
        if num > 0 and 2 <= i < 7:
            pos_ints.append(num)
    return pos_ints