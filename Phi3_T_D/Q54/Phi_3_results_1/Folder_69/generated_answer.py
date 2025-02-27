def all_right_truncatable_prime(numbers):
    x = numbers[760]
    right_truncatable_primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[:-i])):
                return False
        return True
    for num in range(x - 1, 10, -1):
        if is_right_truncatable(num):
            right_truncatable_primes.append(num)
    return right_truncatable_primes