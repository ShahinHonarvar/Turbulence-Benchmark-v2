from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[96]
    right_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        while num_str:
            if not isprime(int(num_str)):
                break
            num_str = num_str[:-1]
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)