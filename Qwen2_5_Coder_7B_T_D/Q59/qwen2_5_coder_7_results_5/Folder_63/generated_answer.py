from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[88]
    limit = 10 ** 8
    primes = []
    for num in range(2, limit):
        if isprime(num):
            str_num = str(num)
            if '0' not in str_num:
                is_left_truncatable = True
                for i in range(len(str_num)):
                    if not isprime(int(str_num[i:])):
                        is_left_truncatable = False
                        break
                if is_left_truncatable:
                    primes.append(num)
    return sorted(primes)