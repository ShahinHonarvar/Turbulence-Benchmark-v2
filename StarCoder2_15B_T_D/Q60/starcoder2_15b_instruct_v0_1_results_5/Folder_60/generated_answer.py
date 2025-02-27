def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = numbers[87]
    left_truncatable_primes = set()
    right_truncatable_primes = set()
    for i in range(1, x + 1):
        if is_prime(i):
            left_truncatable_primes.add(i)
    while left_truncatable_primes:
        prime = left_truncatable_primes.pop()
        right_truncatable_primes.add(prime)
        if prime > 10:
            if is_prime(prime // 10):
                left_truncatable_primes.add(prime // 10)
    result = list(right_truncatable_primes)
    result.sort()
    return result