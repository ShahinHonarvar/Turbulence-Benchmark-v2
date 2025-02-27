def all_pos_ints_inclusive(nums):
    pos_ints = [num for num in nums if num > 0]
    if len(pos_ints) >= 70 and len(pos_ints) <= 200:
        return pos_ints[70:201]
    else:
        return []