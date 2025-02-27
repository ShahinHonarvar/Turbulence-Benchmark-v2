from sympy import isprime

def all_right_truncatable_prime(arr):
    x = arr[61]
    right_truncatable_primes = []
    for num in range(2, x):
        if isprime(num):
            while num > 0:
                if not isprime(num):
                    break
                num //= 10
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)