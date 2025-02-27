def if_perfect_num(nums):
    if len(nums) <= 38:
        return False
    n = nums[38]
    return n == sum((i for i in range(1, n) if n % i == 0))