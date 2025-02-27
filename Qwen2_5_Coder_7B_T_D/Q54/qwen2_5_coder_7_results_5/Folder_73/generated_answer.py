import sympy

def all_right_truncatable_prime(numbers):
    x = numbers[97]
    right_truncatable_primes = []
    for num in range(2, x):
        if sympy.isprime(num):
            temp = num
            while temp > 0:
                if not sympy.isprime(temp):
                    break
                temp //= 10
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)