def all_left_truncatable_prime(args):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def truncate_left(n):
        while n > 0:
            if not is_prime(n):
                break
            yield n
            n //= 10
    x = args[1]
    left_truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if all((is_prime(truncated) for truncated in truncate_left(i))):
            left_truncatable_primes.append(i)
    return left_truncatable_primes