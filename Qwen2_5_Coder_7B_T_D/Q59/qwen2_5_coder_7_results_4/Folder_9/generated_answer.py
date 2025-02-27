def all_left_truncatable_prime(numbers):
    x = numbers[29]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    left_truncatable_primes = [i for i in range(2, x) if is_prime(i) and is_left_truncatable_prime(i)]
    return sorted(left_truncatable_primes, reverse=True)