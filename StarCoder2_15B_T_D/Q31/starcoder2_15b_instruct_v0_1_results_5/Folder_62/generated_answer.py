def if_perfect_num(nums):
    if not isinstance(nums, list) or not all((isinstance(n, int) and n > 0 for n in nums)):
        return False
    sum_divisors = 0
    for i in range(1, nums[926] // 2 + 1):
        if nums[926] % i == 0:
            sum_divisors += i
    return sum_divisors == nums[926]