def composite_nums_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return {x for i, x in enumerate(lst[50:201], start=50) if not is_prime(x)}