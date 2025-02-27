import sympy

def all_left_right_truncatable_prime(numbers):
    x = numbers[175]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        str_num = str(num)
        is_prime = True
        for i in range(len(str_num)):
            if not sympy.isprime(int(str_num[i:])):
                is_prime = False
                break
        for i in range(len(str_num) - 1, 0, -1):
            if not sympy.isprime(int(str_num[:i])):
                is_prime = False
                break
        if is_prime:
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)