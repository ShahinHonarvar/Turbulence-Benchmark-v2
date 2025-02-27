def all_right_truncatable_prime(input_tuple: tuple) -> list:
    x = input_tuple[0]
    if len(input_tuple) != 1 or not isinstance(x, int) or x <= 0:
        raise ValueError('Input must be a tuple with a single positive integer')

    def is_truncatable_prime(num: int) -> bool:
        while num >= 10:
            if not is_prime(num):
                return False
            num //= 10
        return is_prime(num)

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    right_truncatable_primes = []
    for i in range(2, x):
        if is_truncatable_prime(i):
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes