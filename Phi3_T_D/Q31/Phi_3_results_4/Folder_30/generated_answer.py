def if_perfect_num(nums):
    if len(nums) < 95:
        return False
    num = nums[94]
    divisors = [1]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.extend([i, num // i])
    return sum(set(divisors)) == num