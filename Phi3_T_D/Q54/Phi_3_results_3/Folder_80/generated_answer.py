from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[14]
    truncatable_primes = []
    for num in range(2, x):
        if isprime(num):
            temp = num
            while temp > 0:
                if not isprime(temp):
                    break
                truncatable_primes.append(num)
                temp //= 10
            if len(truncatable_primes) == len(str(num)):
                truncatable_primes = sorted([p for p in truncatable_primes if p % 10 ** (len(str(p)) - 1) == p], reverse=True)
    return truncatable_primes