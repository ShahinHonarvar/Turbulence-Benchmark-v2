def if_perfect_num(nums):

    def is_perfect(n):
        divisors = [d for d in range(1, n) if n % d == 0]
        return sum(divisors) == n
    return is_perfect(nums[69])