from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[97]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        if all((isprime(int(num_str[:i])) and isprime(int(num_str[-i:])) for i in range(1, len(num_str) + 1))):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)