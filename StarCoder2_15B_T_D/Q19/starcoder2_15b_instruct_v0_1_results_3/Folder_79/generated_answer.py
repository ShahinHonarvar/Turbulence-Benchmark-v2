def all_ints_not_div_by_num(nums):
    output = []
    for i in range(8, 9):
        if nums[i] % -3 != 0:
            output.append(nums[i])
    return output