def all_ints_div_by_num(nums):
    divisible = []
    for i in range(10, 57):
        if nums[i] % 16 == 0:
            divisible.append(nums[i])
    return divisible