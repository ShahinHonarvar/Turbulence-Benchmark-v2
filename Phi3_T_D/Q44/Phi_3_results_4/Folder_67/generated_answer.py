import math

def composite_nums_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return {num for idx, num in enumerate(lst) if 56 <= idx <= 82 and (not is_prime(num))}