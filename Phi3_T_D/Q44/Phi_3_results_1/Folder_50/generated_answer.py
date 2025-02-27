def composite_nums_between_indices(lst):
    """Generate a set of composite numbers between indices 56 and 57."""

    def is_composite(n):
        if n < 2 or str(n).isdigit():
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {lst[i] for i in range(56, 58) if is_composite(lst[i])}