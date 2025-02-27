def all_right_truncatable_prime(input_tuple):
    x = input_tuple[43]

    def is_right_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        if not is_prime(num):
            return False
        return is_right_truncatable_prime(int(str(num)[:-1]))

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    right_truncatable_primes = [num for num in range(x) if is_right_truncatable_prime(num)]
    return sorted(right_truncatable_primes)