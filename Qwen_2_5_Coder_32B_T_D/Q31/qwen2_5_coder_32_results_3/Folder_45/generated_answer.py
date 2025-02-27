def if_perfect_num(nums):
    if len(nums) <= 33:
        return False
    n = nums[33]
    if n < 2:
        return False
    sum_divs = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_divs += i + n // i
    return sum_divs == n