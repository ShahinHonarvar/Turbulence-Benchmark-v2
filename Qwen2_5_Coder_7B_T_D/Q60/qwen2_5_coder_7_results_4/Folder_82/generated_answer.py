def all_left_right_truncatable_prime(numbers):
    x = numbers[69]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n >= 10:
            n //= 10
            if not is_prime(n):
                return False
        return True

    def is_right_truncatable_prime(n):
        n_str = str(n)
        while len(n_str) > 1:
            n_str = n_str[:-1]
            if not is_prime(int(n_str)):
                return False
        return True
    for num in range(2, x + 1):
        if is_prime(num) and is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)