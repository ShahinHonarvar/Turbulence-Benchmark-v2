def if_perfect_num(nums):
    if len(nums) > 4 and all((isinstance(num, int) and num > 0 for num in nums)):
        n = nums[4]
        sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
        return sum_of_divisors == n
    else:
        return False