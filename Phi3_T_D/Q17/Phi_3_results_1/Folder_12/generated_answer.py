def all_ints_div_by_both_two_nums(nums):
    both_divisible = []
    for num in nums[35:65]:
        if num % -30 == 0 and num % -95 == 0:
            both_divisible.append(num)
    return both_divisible