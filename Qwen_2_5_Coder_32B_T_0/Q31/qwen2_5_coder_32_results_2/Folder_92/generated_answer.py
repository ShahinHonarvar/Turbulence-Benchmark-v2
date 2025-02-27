def if_perfect_num(nums):
    n = nums[0]
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n