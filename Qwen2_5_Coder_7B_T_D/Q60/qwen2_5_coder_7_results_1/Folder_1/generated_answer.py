from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[20]
    truncatable_primes = []

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if '0' in str_n[:i + 1] or '0' in str_n[i:]:
                return False
            if not isprime(int(str_n[:i + 1])) or not isprime(int(str_n[i:])):
                return False
        return True
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)