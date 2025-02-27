def all_left_right_truncatable_prime(max_prime):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(pr):
        str_pr = str(pr)
        for i in range(1, len(str_pr)):
            if not is_prime(int(str_pr[i:])) or not is_prime(int(str_pr[:i])):
                return False
        return True
    truncatable_primes = []
    for i in range(11, max_prime + 1):
        if is_prime(i) and is_truncatable(i):
            truncatable_primes.append(i)
    return truncatable_primes