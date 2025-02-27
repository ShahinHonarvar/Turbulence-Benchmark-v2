def if_perfect_num(nums):
    n = nums[96]
    if n < 2:
        return False
    sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    return sum == n