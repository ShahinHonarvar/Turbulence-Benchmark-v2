from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[88]
    primes = []
    for num in range(2, x):
        if str(num).count('0') == 0 and all((isprime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))):
            primes.append(num)
    return sorted(primes)