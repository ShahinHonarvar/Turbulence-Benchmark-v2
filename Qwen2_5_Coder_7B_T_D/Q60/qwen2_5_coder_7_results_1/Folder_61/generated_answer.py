from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[3]
    truncatable_primes = []

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not isprime(int(str(n)[i:])) or not isprime(int(str(n)[:-i])):
                return False
        return True
    for num in range(2, x + 1):
        if isprime(num) and is_left_right_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)