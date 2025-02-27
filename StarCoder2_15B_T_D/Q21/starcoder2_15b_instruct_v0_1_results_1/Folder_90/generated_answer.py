def all_ints_div_by_num(nums):
    result = []
    for i in range(417, 891):
        if nums[i] % -173 == 0:
            result.append(nums[i])
    return result