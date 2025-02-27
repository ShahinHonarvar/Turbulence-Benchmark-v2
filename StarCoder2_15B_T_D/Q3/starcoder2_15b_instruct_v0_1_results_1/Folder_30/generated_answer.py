def all_pos_ints_inclusive(nums):
    result = []
    for i, num in enumerate(nums):
        if num > 0 and 55 <= i <= 98:
            result.append(num)
    return result