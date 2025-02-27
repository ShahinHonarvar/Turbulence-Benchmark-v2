from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        str_num = str(num)
        is_truncatable = True
        for i in range(len(str_num)):
            if not isprime(int(str_num[i:])) or not isprime(int(str_num[:len(str_num) - i])):
                is_truncatable = False
                break
        if is_truncatable:
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)