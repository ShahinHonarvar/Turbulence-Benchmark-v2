def all_right_truncatable_prime(input_tuple):
    assert isinstance(input_tuple, tuple)
    assert all((isinstance(i, int) and i > 0 for i in input_tuple))
    x = input_tuple[28]

    def is_right_truncatable_prime(num):
        while num >= 10:
            if not is_prime(num):
                return False
            num //= 10
        return is_prime(num)
    right_truncatable_primes = [num for num in range(2, x) if is_right_truncatable_prime(num)]
    return sorted(right_truncatable_primes)

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True