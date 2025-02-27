from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[11]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and isprime(num):
            str_num = str(num)
            is_truncatable = True
            for i in range(len(str_num)):
                if not isprime(int(str_num[i:])) or not isprime(int(str_num[:i + 1])):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)