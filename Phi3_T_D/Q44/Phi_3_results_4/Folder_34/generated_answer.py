from math import sqrt

def composite_nums_between_indices(lst):

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return True
        return False
    return {lst[i] for i in range(70, 201) if is_composite(lst[i])}