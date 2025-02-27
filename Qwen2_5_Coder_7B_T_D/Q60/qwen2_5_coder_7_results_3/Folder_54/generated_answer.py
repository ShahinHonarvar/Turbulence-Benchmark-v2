from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[88]
    lrt_primes = []

    def is_lrt_prime(n):
        if '0' in str(n) or not isprime(n):
            return False
        num_str = str(n)
        while len(num_str) > 1:
            num_str = num_str[1:]
            if not isprime(int(num_str)):
                return False
        num_str = str(n)
        while len(num_str) > 1:
            num_str = num_str[:-1]
            if not isprime(int(num_str)):
                return False
        return True
    for num in range(2, x + 1):
        if is_lrt_prime(num):
            lrt_primes.append(num)
    return sorted(lrt_primes, reverse=True)