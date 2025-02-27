from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[54]
    primes = [2, 3, 5, 7]
    result = []
    for i in range(8, x):
        str_i = str(i)
        if '0' not in str_i and all((isprime(int(str_i[:j])) for j in range(1, len(str_i) + 1))):
            primes.append(i)
            result.append(i)
    return sorted(result)