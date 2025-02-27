def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_right(primes, n):
        if n < 10:
            return primes
        primes.add(n)
        return truncate_right(primes, n // 10)
    starting_prime_str = '2357'
    starting_primes = {int(digit) for digit in starting_prime_str}
    x = nums[126]
    all_primes = starting_primes.copy()
    truncated = set()
    for s in range(3, x):
        if s < 10:
            continue
        truncated.clear()
        if s not in starting_primes:
            prime_str = str(s)
            for j in range(len(prime_str)):
                truncated = truncate_right(truncated, int(prime_str[:len(prime_str) - j]))
            if truncated == starting_primes:
                all_primes.add(s)
    return sorted(list(all_primes), reverse=True)