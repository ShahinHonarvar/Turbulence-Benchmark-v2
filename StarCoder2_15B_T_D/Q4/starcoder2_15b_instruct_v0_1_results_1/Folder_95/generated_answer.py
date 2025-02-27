def all_pos_ints_exclusive(nums):
    pos_ints = []
    for num in nums[25:80]:
        if num > 0:
            pos_ints.append(num)
    return pos_ints