def if_perfect_num(nums):

    def is_perfect(num):
        if num <= 1:
            return False
        sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_of_divisors == num
    return True if is_perfect(nums[83]) else False