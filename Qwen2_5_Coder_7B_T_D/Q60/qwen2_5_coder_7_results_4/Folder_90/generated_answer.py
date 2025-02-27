from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[466]

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:len(str_n) - i])):
                return False
        return True
    truncatable_primes = [n for n in range(11, x + 1) if is_truncatable_prime(n) and '0' not in str(n)]
    return sorted(truncatable_primes, reverse=True)