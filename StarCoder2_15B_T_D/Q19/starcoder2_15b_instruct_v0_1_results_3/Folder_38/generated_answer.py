def all_ints_not_div_by_num(nums):
    output = []
    for i in range(32, 54):
        if nums[i] % -97 != 0:
            output.append(nums[i])
    return output