import math

def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False
    return {num for num in lst[60:201] if is_composite(num)}