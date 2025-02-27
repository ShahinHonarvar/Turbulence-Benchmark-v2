from math import sqrt

def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2 or n % 2 == 0:
            return n > 2
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False
    return {num for num in lst[0:8] if is_composite(num)}