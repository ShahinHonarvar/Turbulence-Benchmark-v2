def if_perfect_num(nums):
    if len(nums) >= 91:
        num = nums[90]
        sum_of_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_of_divisors += i
        return sum_of_divisors == num
    else:
        return False