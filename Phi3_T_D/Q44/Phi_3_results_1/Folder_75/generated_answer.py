def composite_nums_between_indices(num_list):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composites = [n for n in num_list[75:86] if is_composite(n)]
    return set(composites)