def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
            if not is_prime(int(num_str[:len(num_str) - i])):
                return False
        return True
    x = numbers[8]
    truncatable_primes = [n for n in range(2, x + 1) if is_prime(n) and str(n).count('0') == 0 and is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)