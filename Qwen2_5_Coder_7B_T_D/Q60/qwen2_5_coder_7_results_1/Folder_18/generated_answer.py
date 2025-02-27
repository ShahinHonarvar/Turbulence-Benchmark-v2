from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[429]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            is_lr_truncatable = True
            for i in range(len(str_num)):
                if not isprime(int(str_num[i:])) or not isprime(int(str_num[:-i - 1])):
                    is_lr_truncatable = False
                    break
            if is_lr_truncatable:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)