from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    primes = [2, 3, 5, 7]
    for i in range(1, len(str(x))):
        new_primes = []
        for p in primes:
            if p >= 10 ** i:
                continue
            for d in '123456789':
                new_p = p * 10 + int(d)
                if isprime(new_p):
                    new_primes.append(new_p)
        primes.extend(new_primes)
    truncatable_primes = []
    for p in primes:
        num_str = str(p)
        if '0' in num_str:
            continue
        if all((isprime(int(num_str[:i])) and isprime(int(num_str[-i:])) for i in range(1, len(num_str)))):
            truncatable_primes.append(p)
    return sorted(truncatable_primes)