from sympy import isprime

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[38]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            is_left_truncatable = True
            is_right_truncatable = True
            for i in range(len(str_num)):
                if not isprime(int(str_num[i:])):
                    is_left_truncatable = False
                if not isprime(int(str_num[:len(str_num) - i])):
                    is_right_truncatable = False
            if is_left_truncatable and is_right_truncatable:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)