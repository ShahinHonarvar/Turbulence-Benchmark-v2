def if_perfect_num(nums):
    sum_divisors = 0
    num = nums[48]
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num