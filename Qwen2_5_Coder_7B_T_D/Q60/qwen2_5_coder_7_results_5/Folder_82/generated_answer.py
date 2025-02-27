from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[69]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1, 2):
        if '0' not in str(num) and all((isprime(int(str(num)[:i])) and isprime(int(str(num)[i:])) for i in range(1, len(str(num))))):
            primes.append(num)
    return sorted(primes, reverse=True)