def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[618]
    left_truncatable = []
    candidates = set((str(p) for p in range(2, x)))
    for n in candidates.copy():
        if len(n) > 1:
            truncated = n[1:]
            while truncated in candidates:
                if not is_prime(int(truncated)):
                    candidates.discard(truncated)
                    break
                truncated = truncated[1:]
        if is_prime(int(n)):
            left_truncatable.append(int(n))
    return left_truncatable