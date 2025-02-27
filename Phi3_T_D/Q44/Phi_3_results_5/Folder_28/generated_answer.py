def composite_nums_between_indices(int_list):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {x for i, x in enumerate(int_list) if 22 <= i <= 88 and is_composite(x)}