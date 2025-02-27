from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[22]
    primes = [2, 3, 5, 7]
    result = []
    for num in range(11, x, 2):
        str_num = str(num)
        if '0' not in str_num and all((isprime(int(str_num[:i + 1])) for i in range(len(str_num)))):
            primes.append(num)
    for prime in primes:
        if all((isprime(int(str(prime)[i:])) for i in range(len(str(prime))))):
            result.append(prime)
    return sorted(result, reverse=True)