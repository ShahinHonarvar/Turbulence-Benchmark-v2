def all_ints_div_by_both_two_nums(nums):
    divisible_ints = []
    for num in nums:
        if num % 8 == 0 and num % -3 == 0:
            divisible_ints.append(num)
    return divisible_ints