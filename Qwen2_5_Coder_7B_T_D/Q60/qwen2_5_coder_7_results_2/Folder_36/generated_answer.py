from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[992]
    primes = []
    for num in range(2, x + 1):
        if all((isprime(int(str(num)[:i])) and isprime(int(str(num)[i + 1:])) for i in range(len(str(num)) - 1))) and '0' not in str(num):
            primes.append(num)
    return sorted(primes)