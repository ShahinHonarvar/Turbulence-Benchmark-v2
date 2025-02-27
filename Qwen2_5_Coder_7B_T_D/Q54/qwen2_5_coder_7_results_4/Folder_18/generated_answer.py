def all_right_truncatable_prime(nums):
    x = nums[429]
    primes = set(range(2, x))
    for i in range(2, int(x ** 0.5) + 1):
        if i in primes:
            primes.difference_update(range(i * i, x, i))
    right_truncatable = []
    for prime in primes:
        str_prime = str(prime)
        if all((int(str_prime[:i]) in primes for i in range(1, len(str_prime)))):
            right_truncatable.append(prime)
    return sorted(right_truncatable, reverse=True)