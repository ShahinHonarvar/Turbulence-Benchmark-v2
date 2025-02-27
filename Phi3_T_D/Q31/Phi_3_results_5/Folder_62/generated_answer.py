def if_perfect_num(nums):
    if len(nums) >= 927 and all((n > 0 for n in nums)):

        def proper_divisors(n):
            return [i for i in range(1, n // 2 + 1) if n % i == 0]
        return sum(proper_divisors(nums[926])) == nums[926]
    else:
        return False