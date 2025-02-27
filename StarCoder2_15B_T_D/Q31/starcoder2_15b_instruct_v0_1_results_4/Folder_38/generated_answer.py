def if_perfect_num(nums):
    if len(nums) > 38:
        num = nums[38]
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors == num
    else:
        return False