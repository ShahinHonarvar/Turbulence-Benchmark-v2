def all_left_truncatable_prime(x):
    x = x[14]

    def is_left_truncatable_prime(num, prime_set):
        if num < 10 and num in prime_set:
            return True
        elif num % 10 == 0:
            return False
        elif num in prime_set and is_left_truncatable_prime(num // 10, prime_set):
            return True
        else:
            return False
    prime_set = set((i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))))
    return sorted((num for num in prime_set if is_left_truncatable_prime(num, prime_set)))