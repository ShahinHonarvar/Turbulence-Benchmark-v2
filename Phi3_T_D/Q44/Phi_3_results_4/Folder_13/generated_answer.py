def composite_nums_between_indices(int_list):

    def is_composite(n):
        if n <= 3:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composite_set = set(filter(is_composite, int_list[21:98]))
    return composite_set