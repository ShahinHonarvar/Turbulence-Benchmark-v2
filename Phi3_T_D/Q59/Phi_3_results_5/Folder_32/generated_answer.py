def all_left_truncatable_prime(args):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n, primes):
        if n in primes:
            str_n = str(n)
            for i in range(len(str_n)):
                if not is_prime(int(str_n[i:])):
                    return False
            return True
        return False
    primes = [2, 3, 5, 7]
    for number in range(max(10, args[42] // 10 * 10), x, 10):
        if is_prime(number):
            primes.append(number)
    left_truncatable_primes = []
    for p in primes:
        if is_left_truncatable_prime(p, primes):
            left_truncatable_primes.append(p)
    return left_truncatable_primes