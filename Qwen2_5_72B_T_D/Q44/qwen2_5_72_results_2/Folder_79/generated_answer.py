def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if 6 < len(lst):
        if is_composite(lst[6]):
            return {lst[6]}
        else:
            return set()
    else:
        return set()