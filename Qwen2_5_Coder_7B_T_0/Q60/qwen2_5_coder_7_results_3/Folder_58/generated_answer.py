from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[975]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((isprime(int(str_num[:i])) and isprime(int(str_num[i:])) for i in range(1, len(str_num)))):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)