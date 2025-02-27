def all_left_right_truncatable_prime(numbers):
    x = numbers[50]
    truncatables_set = set()

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:i])):
                return False
        return True
    for i in range(23, x + 1):
        if is_prime(i) and is_truncatable(i):
            truncatables_set.add(i)
    return sorted(list(truncatables_set), reverse=True)