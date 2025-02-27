from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[975]
    lr_primes = []
    for num in range(2, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        if all((isprime(int(num_str[:i])) for i in range(1, len(num_str)))):
            if all((isprime(int(num_str[-i:])) for i in range(1, len(num_str)))):
                lr_primes.append(num)
    return sorted(lr_primes, reverse=True)