def if_perfect_num(nums):
    if len(nums) < 52:
        return False
    n = nums[51]
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n