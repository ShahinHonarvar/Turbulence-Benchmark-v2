def all_ints_not_div_by_num(nums):
    result = []
    for i, num in enumerate(nums):
        if i >= 495 and i < 826 and (num % -201 != 0):
            result.append(num)
    return result