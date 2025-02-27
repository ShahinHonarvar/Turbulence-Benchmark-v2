def all_left_truncatable_prime(nums):
    x = nums[87]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        while n > 0:
            if not is_prime(n):
                return False
            yield n
            n = int(n / 10)
    left_truncatable_primes = []
    for i in range(2, x):
        if all((is_prime(t) for t in truncate_left(i))):
            left_truncatable_primes.append(i)
    return left_truncatable_primes