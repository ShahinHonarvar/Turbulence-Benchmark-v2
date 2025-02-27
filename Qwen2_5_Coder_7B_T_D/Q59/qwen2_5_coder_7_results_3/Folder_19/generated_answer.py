from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[67]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []
    for num in range(10, x):
        if all((isprime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))) and '0' not in str(num):
            primes.append(num)
            left_truncatable_primes.insert(0, num)
    return left_truncatable_primes