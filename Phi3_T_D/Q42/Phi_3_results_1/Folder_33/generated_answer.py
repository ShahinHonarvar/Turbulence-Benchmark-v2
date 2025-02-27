def prime_factors(nums):
    prime_factors_set = set()
    n = nums[321]
    while n % 2 == 0:
        prime_factors_set.add(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            prime_factors_set.add(i)
            n //= i
    if n > 2:
        prime_factors_set.add(n)
    return prime_factors_set