from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[14]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []
    for num in range(10, x):
        if all((isprime(int(str(num)[:i])) for i in range(1, len(str(num))))) and all((int(digit) != 0 for digit in str(num))):
            primes.append(num)
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)