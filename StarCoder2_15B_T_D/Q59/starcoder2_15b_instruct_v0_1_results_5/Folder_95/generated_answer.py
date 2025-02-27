def all_left_truncatable_prime(t):
    x = t[0]
    left_truncatable_primes = []

    def is_left_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        if num % 10 == 0:
            return False
        return is_left_truncatable_prime(num // 10) and is_prime(num)

    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for i in range(x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)