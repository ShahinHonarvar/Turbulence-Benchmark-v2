def composite_nums_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_composite(n):
        return n > 1 and (not is_prime(n))
    return {num for index, num in enumerate(lst) if 30 <= index <= 87 and is_composite(num)}