def prime_factors(nums):
    max_num = max(nums)
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    prime_factors = set()
    for i, num in enumerate(nums):
        for j in range(2, num + 1):
            if is_prime[j] and num % j == 0:
                prime_factors.add(j)
    return prime_factors