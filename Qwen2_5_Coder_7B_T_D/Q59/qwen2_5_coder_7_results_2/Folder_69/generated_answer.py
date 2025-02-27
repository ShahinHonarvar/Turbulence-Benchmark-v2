def all_left_truncatable_prime(numbers):
    x = numbers[760]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if int(str_n[i:]) % 2 == 0 or any((digit == '0' for digit in str_n[i:])):
                return False
        return is_prime(n)
    left_truncatable_primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    return sorted(left_truncatable_primes, reverse=True)