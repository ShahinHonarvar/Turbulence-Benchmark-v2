from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[36]
    truncable_primes = []

    def is_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True
    for number in range(2, x):
        if isprime(number) and is_truncatable(number):
            truncable_primes.append(number)
    return sorted(truncable_primes, reverse=True)