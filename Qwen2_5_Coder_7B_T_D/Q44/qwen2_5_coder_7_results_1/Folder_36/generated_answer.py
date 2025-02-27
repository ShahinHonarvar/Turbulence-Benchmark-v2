def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    result = set()
    for i in range(686, 988):
        if 0 <= i < len(lst) and is_composite(lst[i]):
            result.add(lst[i])
    return result