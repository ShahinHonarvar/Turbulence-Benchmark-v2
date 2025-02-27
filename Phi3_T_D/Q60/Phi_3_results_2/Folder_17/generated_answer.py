from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    truncatable_primes = []

    def is_truncatable(prime):
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if not isprime(int(str_prime[i:])) or not isprime(int(str_prime[:i])):
                return False
        return True
    for num in range(2, x + 1):
        if isprime(num) and is_truncatable(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes