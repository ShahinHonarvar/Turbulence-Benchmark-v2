def all_ints_not_div_by_num(nums):
    output = []
    for i in range(81, 86):
        if nums[i] % 77 != 0:
            output.append(nums[i])
    return output