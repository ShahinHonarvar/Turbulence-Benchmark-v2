def is_perfect(n):
    return sum((i for i in range(1, n) if n % i == 0)) == n

def if_perfect_num(nums):
    return is_perfect(nums[410]) if len(nums) > 410 else False