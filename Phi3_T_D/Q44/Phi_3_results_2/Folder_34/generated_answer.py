from math import sqrt

def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False
    return {n for n in numbers[70:201] if is_composite(n)}