def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    start, end = (533, 605)
    return {lst[i] for i in range(start, end + 1) if is_composite(lst[i])}