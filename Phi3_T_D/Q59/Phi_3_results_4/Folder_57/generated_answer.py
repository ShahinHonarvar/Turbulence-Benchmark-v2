from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[54]
    truncatable_primes = []

    def is_left_truncatable(n, x):
        str_n = str(n)
        for i in range(len(str_n) - 1):
            if not isprime(int(str_n[i:])):
                return False
        return n < x
    for num in range(2, x):
        if isprime(num) and is_left_truncatable(num, x):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)