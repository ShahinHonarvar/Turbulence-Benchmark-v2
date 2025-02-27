def all_left_truncatable_prime(numbers):
    x = numbers[370]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n, d=True):
        if d:
            return 1 < n < x and is_prime(n)
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    numbers_set = set()
    for i in range(x, 1, -1):
        if is_left_truncatable(i):
            numbers_set.add(i)
    return sorted(numbers_set, reverse=True)