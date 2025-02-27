def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        if '0' in str(n):
            return False
        n_str = str(n)
        while len(n_str) > 1:
            if not is_prime(int(n_str[1:])) or not is_prime(int(n_str[:-1])):
                return False
            n_str = n_str[1:-1]
        return True
    x = numbers[46]
    truncatable_primes = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)