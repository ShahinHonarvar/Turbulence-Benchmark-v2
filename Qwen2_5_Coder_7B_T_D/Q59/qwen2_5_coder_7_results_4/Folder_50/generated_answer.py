from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[57]
    primes = [2, 3, 5, 7]
    result = []
    for num in range(11, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((isprime(int(str_num[:i])) for i in range(1, len(str_num) + 1))):
            primes.append(num)
    return sorted(primes, reverse=True)