def all_ints_div_by_num(nums):
    divisible_ints = []
    for i, num in enumerate(nums):
        if num % -14 == 0 and 66 <= i <= 74:
            divisible_ints.append(num)
    return divisible_ints