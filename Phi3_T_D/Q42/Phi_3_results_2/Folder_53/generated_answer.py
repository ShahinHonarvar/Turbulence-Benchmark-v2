def prime_factors(nums):
    if len(nums) > 73:
        num = nums[73]
        i = 2
        factors = set()
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                factors.add(i)
        if num > 1:
            factors.add(num)
        return factors
    else:
        return 'Index out of range'