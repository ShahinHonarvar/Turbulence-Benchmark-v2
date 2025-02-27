def all_right_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[38]

    def is_right_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        return is_prime(num) and is_right_truncatable_prime(num // 10)

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    right_truncatable_primes = [num for num in range(10, x) if is_right_truncatable_prime(num)]
    return sorted(right_truncatable_primes, reverse=True)