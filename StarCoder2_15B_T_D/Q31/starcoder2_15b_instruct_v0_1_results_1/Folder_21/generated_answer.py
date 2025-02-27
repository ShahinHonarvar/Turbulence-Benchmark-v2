def if_perfect_num(nums):
    if len(nums) > 410:
        num = nums[410]
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        if sum_divisors == num:
            return True
    return False