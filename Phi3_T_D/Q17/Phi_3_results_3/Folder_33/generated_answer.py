def all_ints_div_by_both_two_nums(nums):
    factor1 = -722
    factor2 = -731
    divisible_nums = [num for num in nums[281:695] if num % factor1 == 0 and num % factor2 == 0]
    return divisible_nums