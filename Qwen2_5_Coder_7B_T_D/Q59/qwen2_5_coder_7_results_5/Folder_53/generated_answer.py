def all_left_truncatable_prime(numbers):
    x = numbers[86]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_primes = [p for p in primes if is_left_truncatable_prime(p)]
    return sorted(left_truncatable_primes, reverse=True)