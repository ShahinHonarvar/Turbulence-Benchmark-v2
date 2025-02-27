def if_perfect_num(nums):
    perfect = lambda n: sum((i for i in range(1, n // 2 + 1) if n % i == 0)) == n
    return perfect(nums[67]) if len(nums) > 67 else False