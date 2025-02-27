from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[28]
    right_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        is_right_truncatable = True
        for i in range(len(num_str)):
            if not isprime(int(num_str[:len(num_str) - i])):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)