from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[61]
    limit = 10 ** len(str(x))
    left_truncatable_primes = []
    for num in range(2, limit):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((isprime(int(str_num[:i + 1])) for i in range(len(str_num)))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)