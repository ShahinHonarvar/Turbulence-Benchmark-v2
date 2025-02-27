def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncate(n):
        n = str(n)
        return [int(n[i:]) for i in range(len(n))]

    def left_truncatable(n):
        if not is_prime(n):
            return False
        truncated = right_truncate(n)
        return all((is_prime(t) for t in truncated))
    x = numbers[52]
    return sorted([n for n in range(2, x) if left_truncatable(n)], reverse=True)