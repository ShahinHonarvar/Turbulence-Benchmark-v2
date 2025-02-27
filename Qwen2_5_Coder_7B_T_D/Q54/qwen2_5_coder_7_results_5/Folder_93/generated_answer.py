from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[11]
    right_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        if all((isprime(int(num_str[:i + 1])) for i in range(len(num_str)))):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)