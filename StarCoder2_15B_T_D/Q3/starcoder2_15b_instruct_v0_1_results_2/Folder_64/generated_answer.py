def all_pos_ints_inclusive(nums):
    result = []
    for num in nums[:5]:
        if num > 0:
            result.append(num)
    return result