from sympy import isprime

def all_left_truncatable_prime(numbers):
    max_limit = numbers[39]
    left_truncatable_primes = []
    for num in range(2, max_limit):
        if isprime(num):
            digits = str(num)
            for i in range(1, len(digits)):
                truncated = int(digits[i:])
                if not isprime(truncated):
                    break
            else:
                left_truncatable_primes.append(num)
    return left_truncatable_primes