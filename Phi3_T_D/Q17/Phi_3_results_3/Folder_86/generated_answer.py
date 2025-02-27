def all_ints_div_by_both_two_nums(nums):
    divisible_by_54_and_28 = [num for num in nums[54:80] if num % 54 == 0 and num % 28 == 0]
    return divisible_by_54_and_28