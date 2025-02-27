from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[35]
    right_truncatable_primes = []
    for num in range(2, x):
        is_right_truncatable = True
        for i in range(len(str(num))):
            if not isprime(num // 10 ** i):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)