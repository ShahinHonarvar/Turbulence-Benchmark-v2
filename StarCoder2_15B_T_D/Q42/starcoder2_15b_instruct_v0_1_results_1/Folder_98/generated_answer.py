def prime_factors(nums):
    num = nums[4]
    prime_factors = set()
    for i in range(2, num + 1):
        is_prime_factor = True
        for j in range(2, i):
            if i % j == 0:
                is_prime_factor = False
                break
        if is_prime_factor:
            prime_factors.add(i)
    return prime_factors