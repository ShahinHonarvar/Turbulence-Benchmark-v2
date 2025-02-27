def composite_nums_between_indices(l):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {n for i, n in enumerate(l) if 56 <= i <= 82 and is_composite(n)}