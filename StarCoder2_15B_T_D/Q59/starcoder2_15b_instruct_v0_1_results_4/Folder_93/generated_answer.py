def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(num):

    def helper(n, primes):
        if is_prime(n):
            primes.append(n)
            helper(n // 10, primes)
    primes = []
    helper(num, primes)
    return primes