def composite_nums_between_indices(integers):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {n for i, n in enumerate(integers) if is_composite(n) and 26 <= i <= 52}