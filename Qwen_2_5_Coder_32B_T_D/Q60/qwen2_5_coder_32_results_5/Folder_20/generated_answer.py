def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable_prime(n):
        ns = str(n)
        if '0' in ns:
            return False
        for i in range(1, len(ns)):
            if not is_prime(int(ns[i:])) or not is_prime(int(ns[:-i])):
                return False
        return True
    x = numbers[100]
    result = [n for n in range(2, x + 1) if is_lr_truncatable_prime(n)]
    return sorted(result, reverse=True)