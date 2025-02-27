def prime_factors(nums):
    num = nums[453]
    prime_factors = set()
    i = 2
    while i * i <= num:
        while num % i == 0:
            prime_factors.add(i)
            num //= i
        i += 1
    if num > 1:
        prime_factors.add(num)
    return prime_factors