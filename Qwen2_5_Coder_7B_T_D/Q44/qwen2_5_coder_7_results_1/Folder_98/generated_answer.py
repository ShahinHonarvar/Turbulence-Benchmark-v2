from math import sqrt

def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False
    return {x for x in lst[:7] if is_composite(x)}