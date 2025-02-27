from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[86]
    left_truncatable_primes = []

    def is_left_truncatable(prime):
        num_str = str(prime)
        while num_str:
            if '0' in num_str or not isprime(int(num_str)):
                return False
            num_str = num_str[1:]
        return True
    for num in range(2, x):
        if isprime(num) and is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)