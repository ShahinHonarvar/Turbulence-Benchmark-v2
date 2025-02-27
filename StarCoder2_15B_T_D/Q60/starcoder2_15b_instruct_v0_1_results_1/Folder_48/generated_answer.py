def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[835]

    def is_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        if num % 10 == 0 or not is_prime(num):
            return False
        return is_truncatable_prime(num // 10)

    def is_prime(num):
        if num < 2:
            return False
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                return False
        return True
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)