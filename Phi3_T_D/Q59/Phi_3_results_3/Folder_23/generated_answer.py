def all_left_truncatable_prime(num_tuple):
    x = num_tuple[77]
    left_truncatable = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n, s):
        while n > 0:
            if not is_prime(int(s)):
                return False
            n, digit = divmod(n, 10)
            s = str(digit) + s
        return True
    for number in range(x - 1, 1, -1):
        if str(number).startswith('0') or not is_prime(number):
            continue
        if is_truncatable(number, ''):
            left_truncatable.append(number)
    return left_truncatable