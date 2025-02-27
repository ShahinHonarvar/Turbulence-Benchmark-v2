from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[18]
    right_truncatable_primes = []
    for num in range(2, x):
        if isprime(num):
            num_str = str(num)
            while len(num_str) > 1 and isprime(int(num_str)):
                num_str = num_str[:-1]
            if len(num_str) == 1:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)