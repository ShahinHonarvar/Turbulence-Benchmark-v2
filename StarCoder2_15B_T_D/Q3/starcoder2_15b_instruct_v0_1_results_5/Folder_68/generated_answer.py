def all_pos_ints_inclusive(nums):
    pos_ints = []
    for num in nums:
        if num > 0:
            pos_ints.append(num)
    return pos_ints[:9]