from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[97]
    left_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' not in str_num and all((isprime(int(str_num[:i])) for i in range(1, len(str_num) + 1))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)