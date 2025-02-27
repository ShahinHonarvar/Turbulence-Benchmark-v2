from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[79]
    limit = x
    primes = [2, 3, 5, 7]
    result = []
    for num in range(11, limit):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((isprime(int(str_num[:i + 1])) for i in range(len(str_num)))):
            primes.append(num)
            result.append(num)
    result.sort(reverse=True)
    return result