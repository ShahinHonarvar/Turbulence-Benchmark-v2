def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[:len(str(n)) - i])):
                return False
        return True
    x = numbers[126]
    right_trunc_primes = [n for n in range(x) if is_right_truncatable_prime(n)]
    return sorted(right_trunc_primes, reverse=True)