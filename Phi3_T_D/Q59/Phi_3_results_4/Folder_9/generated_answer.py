from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[29]
    truncatable_primes = []

    def is_left_truncatable(prime):
        str_prime = str(prime)
        for i in range(len(str_prime)):
            if not isprime(int(str_prime[i:])):
                return False
        return True
    for number in range(x - 1, 1, -1):
        if isprime(number) and is_left_truncatable(number):
            truncatable_primes.append(number)
    return truncatable_primes