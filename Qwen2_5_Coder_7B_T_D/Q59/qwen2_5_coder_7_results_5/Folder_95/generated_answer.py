from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[77]
    left_truncatable_primes = []

    def is_left_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if '0' in str_n[:i + 1] or not isprime(int(str_n[:i + 1])):
                return False
        return True
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)