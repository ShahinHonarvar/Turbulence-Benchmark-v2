def if_perfect_num(nums):
    if len(nums) > 3 and all((isinstance(num, int) and num > 0 for num in nums)):
        n = nums[3]
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    return False