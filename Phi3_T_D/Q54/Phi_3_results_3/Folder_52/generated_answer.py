def all_right_truncatable_prime(numbers):
    x = numbers[52]
    right_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    for num in range(x - 1, 10, -1):
        num_str = str(num)
        if is_right_truncatable_prime(num) and num_str[-1] in '73579':
            right_truncatable_primes.append(num)
    return right_truncatable_primes