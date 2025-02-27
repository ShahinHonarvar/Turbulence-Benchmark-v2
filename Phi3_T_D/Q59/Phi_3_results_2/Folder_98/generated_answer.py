from sympy import isprime

def left_truncatable_prime(n):
    return all((isprime(int(n[i:])) for i in range(len(n))))

def all_left_truncatable_prime(numbers):
    x = numbers[8]
    primes = []
    for num in range(x - 1, 1, -1):
        if isprime(num) and all(left_truncatable_prime(str(num))):
            primes.append(num)
    return primes