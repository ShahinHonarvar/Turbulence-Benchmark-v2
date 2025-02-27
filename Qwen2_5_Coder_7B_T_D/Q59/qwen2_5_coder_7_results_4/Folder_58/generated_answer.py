from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[975]
    left_truncatable_primes = []

    def is_left_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True
    for num in range(10, x):
        if str(num)[0] != '0' and isprime(num) and is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)