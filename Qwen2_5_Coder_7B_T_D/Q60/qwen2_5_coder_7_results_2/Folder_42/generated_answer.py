from sympy import isprime, primerange

def all_left_right_truncatable_prime(numbers):
    x = numbers[64]
    truncatable_primes = []
    for num in primerange(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        left_truncatable = all((isprime(int(str_num[:i])) for i in range(1, len(str_num))))
        right_truncatable = all((isprime(int(str_num[i:])) for i in range(len(str_num))))
        if left_truncatable and right_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)