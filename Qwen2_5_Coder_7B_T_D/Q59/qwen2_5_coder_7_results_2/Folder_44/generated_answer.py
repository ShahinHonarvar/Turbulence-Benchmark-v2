from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[39]
    left_truncatable_primes = []

    def is_left_truncatable_prime(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if '0' in num_str[:i + 1]:
                return False
            if not isprime(int(num_str[:i + 1])):
                return False
        return True
    for num in range(2, x):
        if isprime(num) and is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)