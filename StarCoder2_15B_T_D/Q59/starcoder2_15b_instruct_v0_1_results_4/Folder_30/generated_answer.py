def all_left_truncatable_prime(input_tuple):
    x = input_tuple[37]

    def is_left_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        else:
            return is_prime(n) and is_left_truncatable_prime(n % 10)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for i in range(x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)