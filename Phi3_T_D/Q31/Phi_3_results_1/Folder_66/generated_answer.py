def is_perfect(n):
    sum_div = sum((i for i in range(1, n) if n % i == 0))
    return sum_div == n

def if_perfect_num(nums):
    return is_perfect(nums[42]) if len(nums) > 42 else False