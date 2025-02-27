import sympy

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and sympy.isprime(num):
            str_num = str(num)
            is_left_right_truncatable = True
            for i in range(len(str_num)):
                if not sympy.isprime(int(str_num[i:])) or not sympy.isprime(int(str_num[:len(str_num) - i])):
                    is_left_right_truncatable = False
                    break
            if is_left_right_truncatable:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)