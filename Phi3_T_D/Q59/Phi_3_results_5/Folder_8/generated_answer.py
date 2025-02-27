def all_left_truncatable_prime(numbers):
    x = numbers[41]
    left_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(number):
        str_num = str(number)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True
    for prime in range(x, 0, -1):
        if is_prime(prime) and is_left_truncatable(prime):
            left_truncatable_primes.append(prime)
    return left_truncatable_primes