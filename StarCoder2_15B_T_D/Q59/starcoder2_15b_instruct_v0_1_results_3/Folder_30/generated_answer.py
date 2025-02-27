def all_left_truncatable_prime(x):
    n = x[37]

    def is_truncatable_prime(num, prime_set):
        if num < 10 and num in prime_set:
            return True
        elif num % 10 == 0:
            return False
        elif num in prime_set:
            return is_truncatable_prime(num // 10, prime_set)
        else:
            return False
    prime_set = set()
    for i in range(2, n + 1):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            prime_set.add(i)
    return sorted(filter(lambda num: is_truncatable_prime(num, prime_set), prime_set), reverse=True)