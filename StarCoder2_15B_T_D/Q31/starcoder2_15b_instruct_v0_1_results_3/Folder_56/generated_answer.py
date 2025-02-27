def if_perfect_num(nums):

    def is_perfect_num(num):
        sum_of_divisors = 0
        for divisor in range(1, num):
            if num % divisor == 0:
                sum_of_divisors += divisor
        return sum_of_divisors == num
    return is_perfect_num(nums[60])