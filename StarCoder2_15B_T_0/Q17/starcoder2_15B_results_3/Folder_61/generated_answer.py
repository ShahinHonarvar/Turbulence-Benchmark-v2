def all_ints_div_by_both_two_nums(nums):
    return [num for num in nums if num % (-5 * -6) == 0 and 0 <= nums.index(num) <= 6]