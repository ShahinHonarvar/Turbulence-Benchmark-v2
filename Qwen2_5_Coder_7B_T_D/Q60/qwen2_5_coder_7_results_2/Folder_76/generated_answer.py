from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[370]
    truncatable_primes = []
    for num in range(2, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        if all((isprime(int(num_str[:i])) and isprime(int(num_str[i:])) for i in range(1, len(num_str)))):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)