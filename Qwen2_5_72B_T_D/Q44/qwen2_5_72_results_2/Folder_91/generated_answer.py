def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(lst) < 6:
        return set()
    if is_composite(lst[5]):
        return {lst[5]}
    return set()