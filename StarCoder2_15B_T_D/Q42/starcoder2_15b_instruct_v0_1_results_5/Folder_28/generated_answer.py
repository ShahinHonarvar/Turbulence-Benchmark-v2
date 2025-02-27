def prime_factors(nums):
    number = nums[37]
    factors = set()
    for i in range(2, int(number ** 0.5) + 1):
        while number % i == 0:
            factors.add(i)
            number //= i
    if number > 1:
        factors.add(number)
    return factors