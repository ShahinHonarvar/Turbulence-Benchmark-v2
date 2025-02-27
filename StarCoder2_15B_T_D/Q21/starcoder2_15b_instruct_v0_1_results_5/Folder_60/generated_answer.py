def all_ints_div_by_num(nums):
    divisible_ints = []
    for i, num in enumerate(nums):
        if i >= 31 and i <= 67 and (num % -15 == 0):
            divisible_ints.append(num)
    return divisible_ints