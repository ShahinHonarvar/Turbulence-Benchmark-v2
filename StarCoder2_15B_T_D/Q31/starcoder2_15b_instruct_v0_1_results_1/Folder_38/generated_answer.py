def if_perfect_num(nums):
    if 38 < len(nums):
        num = nums[38]
        sum_of_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_of_divisors += i
        return sum_of_divisors == num
    else:
        return False