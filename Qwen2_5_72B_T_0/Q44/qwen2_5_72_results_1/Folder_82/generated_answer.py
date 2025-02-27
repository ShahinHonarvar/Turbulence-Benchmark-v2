def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if 30 < len(lst):
        result = set()
        if is_composite(lst[30]):
            result.add(lst[30])
        return result
    return set()