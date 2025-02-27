def if_perfect_num(nums):
    if len(nums) > 56 and all((isinstance(num, int) and num > 0 for num in nums)):
        n = nums[56]
        divisors = [i for i in range(1, n // 2 + 1) if n % i == 0]
        return sum(divisors) == n
    return False