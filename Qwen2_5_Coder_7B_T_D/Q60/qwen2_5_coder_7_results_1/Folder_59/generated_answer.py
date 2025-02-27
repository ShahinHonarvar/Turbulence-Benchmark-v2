from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[84]
    truncatable_primes = []
    for num in range(2, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        left_truncatable = True
        right_truncatable = True
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])):
                left_truncatable = False
            if not isprime(int(num_str[:len(num_str) - i])):
                right_truncatable = False
            if not left_truncatable and (not right_truncatable):
                break
        if left_truncatable and right_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)