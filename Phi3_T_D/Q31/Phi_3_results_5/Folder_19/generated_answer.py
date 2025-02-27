def if_perfect_num(nums):
    perfect = lambda n: sum((i for i in range(1, n) if n % i == 0)) == n
    return 13 < len(nums) and perfect(nums[13])