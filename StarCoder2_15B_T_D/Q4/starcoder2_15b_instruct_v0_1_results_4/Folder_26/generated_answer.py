def all_pos_ints_exclusive(nums):
    result = []
    for i, num in enumerate(nums):
        if num > 0 and 44 < i < 78:
            result.append(num)
    return result