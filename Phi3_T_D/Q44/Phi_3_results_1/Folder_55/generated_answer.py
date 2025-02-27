import math

def composite_nums_between_indices(lst):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    composite_numbers = {x for x in lst[10:101] if not is_prime(x)}
    return composite_numbers