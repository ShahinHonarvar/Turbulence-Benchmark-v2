from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[784]
    truncatable_primes = []

    def is_truncatable_prime(n):
        if not n:
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:-i])):
                return False
        return isprime(n)
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes