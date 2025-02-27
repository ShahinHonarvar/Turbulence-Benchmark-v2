from sympy import isprime

def is_left_right_truncatable_prime(n):
    if n < 10:
        return False
    num_str = str(n)
    if '0' in num_str:
        return False
    for i in range(len(num_str)):
        left_truncated = int(num_str[i:])
        right_truncated = int(num_str[:len(num_str) - i])
        if not isprime(left_truncated) or not isprime(right_truncated):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[177]
    truncatable_primes = []
    for num in range(10, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)