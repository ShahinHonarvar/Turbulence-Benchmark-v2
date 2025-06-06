def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        s = str(n)
        return all((is_prime(int(s[i:])) for i in range(len(s))))
    x = numbers[97]
    left_truncatable_primes = [n for n in range(2, x) if '0' not in str(n) and is_left_truncatable_prime(n)]
    return sorted(left_truncatable_primes, reverse=True)