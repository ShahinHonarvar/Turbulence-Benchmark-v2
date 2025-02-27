from sympy import primerange

def all_left_right_truncatable_prime(numbers):
    x = numbers[126]
    primes = list(primerange(2, x + 1))
    lr_truncatable_primes = []

    def is_lr_truncatable(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if '0' in num_str[i:]:
                return False
            if not is_prime(int(num_str[i:])):
                return False
            if not is_prime(int(num_str[:-i])):
                return False
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for prime in primes:
        if is_lr_truncatable(prime):
            lr_truncatable_primes.append(prime)
    return sorted(lr_truncatable_primes, reverse=True)