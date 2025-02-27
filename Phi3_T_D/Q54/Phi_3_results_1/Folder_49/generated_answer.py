from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[14]
    primes = [num for num in range(2, x) if isprime(num)]
    right_truncatables = []
    for prime in primes:
        str_prime = str(prime)
        while str_prime:
            if not isprime(int(str_prime)):
                break
            right_truncatables.append(prime)
            str_prime = str_prime[:-1]
    return sorted(set(right_truncatables))