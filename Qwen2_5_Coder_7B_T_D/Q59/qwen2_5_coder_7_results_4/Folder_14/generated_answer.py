from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[78]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        if isprime(num):
            temp = num
            while temp > 0:
                if not isprime(temp):
                    break
                temp //= 10
            else:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)