from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[64]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []
    for num in range(11, x):
        if all((isprime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))) and '0' not in str(num):
            primes.append(num)
            for p in primes:
                if isprime(int(str(num) + str(p))):
                    primes.append(int(str(num) + str(p)))
    for p in primes:
        if all((isprime(int(str(p)[:i])) for i in range(1, len(str(p)) + 1))) and '0' not in str(p):
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes, reverse=True)