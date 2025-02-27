from math import sqrt

def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False
    composites = {num for num in lst[28:41] if is_composite(num)}
    return composites