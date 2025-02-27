def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(lst) < 3:
        return set()
    result = set()
    if is_composite(lst[2]):
        result.add(lst[2])
    return result