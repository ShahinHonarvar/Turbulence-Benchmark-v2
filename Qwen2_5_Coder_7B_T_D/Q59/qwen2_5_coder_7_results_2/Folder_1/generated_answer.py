from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[20]
    left_truncatable_primes = []
    for num in range(2, x):
        if str(num).count('0') == 0 and all((isprime(int(str(num)[i:])) for i in range(len(str(num))))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)