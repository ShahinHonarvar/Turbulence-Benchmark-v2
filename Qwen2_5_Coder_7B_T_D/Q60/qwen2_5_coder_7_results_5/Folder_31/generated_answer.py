from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[50]
    truncatable_primes = []

    def is_truncatable_prime(num):
        s = str(num)
        for i in range(len(s)):
            if '0' in s[i:] or not isprime(int(s[i:])):
                return False
        for i in range(len(s)):
            if '0' in s[:i + 1] or not isprime(int(s[:i + 1])):
                return False
        return True
    for num in range(2, x + 1):
        if isprime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)