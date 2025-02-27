def if_perfect_num(nums):

    def is_perfect(num):
        divisors = [d for d in range(1, num) if num % d == 0]
        return sum(divisors) == num
    return is_perfect(nums[222])