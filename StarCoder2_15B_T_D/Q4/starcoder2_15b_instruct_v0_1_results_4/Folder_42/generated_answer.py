def all_pos_ints_exclusive(nums):
    output = []
    for i, num in enumerate(nums):
        if num > 0 and i >= 44 and (i < 67):
            output.append(num)
    return output