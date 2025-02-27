from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[758]
    primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if isprime(int(str_num)):
            is_truncatable = True
            for i in range(1, len(str_num)):
                if not isprime(int(str_num[i:])) or not isprime(int(str_num[:-i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                primes.append(num)
    return sorted(primes)