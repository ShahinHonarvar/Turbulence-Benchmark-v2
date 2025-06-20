def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    result = set()
    if len(lst) > 57:
        for i in range(56, 58):
            if is_composite(lst[i]):
                result.add(lst[i])
    return result