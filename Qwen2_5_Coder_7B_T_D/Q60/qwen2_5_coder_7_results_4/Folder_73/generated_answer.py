from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[97]
    primes = [num for num in range(2, x + 1) if isprime(num) and '0' not in str(num)]
    truncatable_primes = []
    for p in primes:
        str_p = str(p)
        if all((isprime(int(str_p[:i])) for i in range(1, len(str_p)))) and all((isprime(int(str_p[-i:])) for i in range(1, len(str_p)))):
            truncatable_primes.append(p)
    return sorted(truncatable_primes)