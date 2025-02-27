def all_ints_div_by_num(nums):
    output = []
    for i in range(59, 78):
        if nums[i] % -95 == 0:
            output.append(nums[i])
    return output