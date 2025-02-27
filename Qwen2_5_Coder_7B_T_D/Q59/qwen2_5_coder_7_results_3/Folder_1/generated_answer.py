from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[20]

    def is_left_truncatable_prime(num):
        if '0' in str(num) or not isprime(num):
            return False
        for i in range(len(str(num))):
            if not isprime(int(str(num)[i:])):
                return False
        return True
    left_truncatable_primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    return sorted(left_truncatable_primes, reverse=True)