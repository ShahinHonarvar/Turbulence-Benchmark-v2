from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[57]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if all((isprime(int(num[:i])) for i in range(1, len(num) + 1))):
            primes.append(int(num))
    return sorted(primes, reverse=True)