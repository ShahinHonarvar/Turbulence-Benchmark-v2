def all_right_truncatable_prime(t):
    x = t[7]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(11, x):
        if all((is_prime(int(str(num)[-i - 1:])) for i in range(len(str(num))))):
            primes.append(num)
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)