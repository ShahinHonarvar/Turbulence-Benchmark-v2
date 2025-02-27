def if_perfect_num(nums):

    def is_perfect(n):
        sum_factors = sum((i for i in range(1, n) if n % i == 0))
        return sum_factors == n
    return is_perfect(nums[53]) if len(nums) > 53 else False