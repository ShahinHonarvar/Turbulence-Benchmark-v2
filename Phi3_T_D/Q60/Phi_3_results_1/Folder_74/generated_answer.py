def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        return all((is_prime(int(s[i:])) and is_prime(int(s[:i + 1])) for i in range(len(s))))
    x = numbers[36]
    truncatable_primes = [i for i in range(2, x + 1) if is_truncatable_prime(i)]
    return truncatable_primes