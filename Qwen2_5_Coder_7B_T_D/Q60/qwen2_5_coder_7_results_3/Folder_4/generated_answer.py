from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[96]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and all((isprime(int(str(num)[:i])) and isprime(int(str(num)[-i:])) for i in range(1, len(str(num)) + 1))):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)