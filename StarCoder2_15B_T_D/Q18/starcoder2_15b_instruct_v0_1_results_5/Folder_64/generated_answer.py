def sum_ints_div_by_either_nums(nums):
    sum_divisible = 0
    for num in nums:
        if num % 11 == 0 or num % -7 == 0:
            sum_divisible += num
        if nums.index(num) == 3:
            return sum_divisible
    return sum_divisible