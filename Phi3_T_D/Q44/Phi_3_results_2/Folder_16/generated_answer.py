def composite_nums_between_indices(integers):

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    return {n for n in integers[40:81] if is_composite(n)}