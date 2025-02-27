def if_perfect_num(nums):
    n = nums[0]
    return sum((i for i in range(1, n) if n % i == 0)) == n