def composite_nums_between_indices(lst):

    def is_composite(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composite_set = {lst[i] for i in range(59, 98)}
    composite_set = {num for num in composite_set if is_composite(num)}
    return composite_set