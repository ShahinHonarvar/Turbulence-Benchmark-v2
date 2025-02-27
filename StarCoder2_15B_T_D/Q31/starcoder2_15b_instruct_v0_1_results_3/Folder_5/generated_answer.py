def if_perfect_num(nums):
    sum_of_divisors = 0
    num = nums[67]
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num