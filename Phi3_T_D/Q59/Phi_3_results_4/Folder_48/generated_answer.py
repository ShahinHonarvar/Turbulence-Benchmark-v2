def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n, prime_set):
        if not is_prime(n):
            return False
        if n < 10:
            return True
        return is_left_truncatable_prime(int(str(n)[1:]), prime_set)
    limit = numbers[835]
    prime_set = {2, 3, 5, 7}
    for i in range(11, limit, 2):
        if is_prime(i):
            prime_set.add(i)
    left_truncatable = [p for p in prime_set if is_left_truncatable_prime(p, prime_set)]
    return left_truncatable