from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[55]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if all((isprime(int(str(num)[:i])) and isprime(int(str(num)[i:])) for i in range(1, len(str(num))))) and isprime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)