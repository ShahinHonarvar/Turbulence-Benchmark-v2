def sum_ints_div_by_either_nums(nums):
    divisor1, divisor2 = (858, 952)
    start, end = (299, 382)
    return sum((num for num in nums[start:end + 1] if num % divisor1 == 0 or num % divisor2 == 0))