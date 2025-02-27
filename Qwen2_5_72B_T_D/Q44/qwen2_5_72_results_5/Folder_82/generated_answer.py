def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if 30 < 0 or 30 >= len(lst):
        return set()
    return {lst[30]} if is_composite(lst[30]) else set()