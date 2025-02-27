def if_perfect_num(nums):

    def is_perfect_num(n):
        sum_factors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_factors += i
        return sum_factors == n
    return is_perfect_num(nums[95])