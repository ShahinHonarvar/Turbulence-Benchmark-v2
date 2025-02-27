from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[35]
    limit = 10 ** len(str(x))
    primes = []
    for num in range(11, limit, 2):
        str_num = str(num)
        if '0' in str_num:
            continue
        while str_num:
            if not isprime(int(str_num)):
                break
            str_num = str_num[1:]
        else:
            primes.append(num)
    return sorted(primes, reverse=True)