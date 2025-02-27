def if_perfect_num(nums):

    def check_perfect(num):
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0:
                sum_divisors += i
        return sum_divisors == num
    return check_perfect(nums[162])