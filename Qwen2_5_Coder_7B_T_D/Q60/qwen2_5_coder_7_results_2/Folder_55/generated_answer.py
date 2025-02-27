def all_left_right_truncatable_prime(numbers):
    x = numbers[73]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:len(num_str) - i])):
                return False
        return True
    primes = [n for n in range(2, x + 1) if is_prime(n)]
    left_right_truncatable_primes = [p for p in primes if is_left_right_truncatable(p)]
    return sorted(left_right_truncatable_primes, reverse=True)