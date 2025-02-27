def if_perfect_num(nums):
    n = nums[19]
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n