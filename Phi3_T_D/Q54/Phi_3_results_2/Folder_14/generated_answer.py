def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n % 2 == 0 and n > 2:
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True
    x = numbers[78]
    right_truncatable_primes = [num for num in range(x) if is_prime(num) and is_right_truncatable_prime(num)]
    return sorted(right_truncatable_primes, reverse=True)