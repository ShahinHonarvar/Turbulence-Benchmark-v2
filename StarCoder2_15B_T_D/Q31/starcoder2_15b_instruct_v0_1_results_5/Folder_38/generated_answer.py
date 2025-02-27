def if_perfect_num(nums):
    if len(nums) <= 38:
        return False
    num = nums[38]
    sum_divisors = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num