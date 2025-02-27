def if_perfect_num(nums):
    if len(nums) <= 27:
        return False
    n = nums[27]
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n