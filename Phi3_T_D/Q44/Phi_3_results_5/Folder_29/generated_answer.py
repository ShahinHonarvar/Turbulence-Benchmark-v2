from math import sqrt

def composite_nums_between_indices(num_list):
    composite_set = set()

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    start = 52
    end = 71
    for i in range(start, end + 1):
        if not is_prime(num_list[i]) and num_list[i] > 1:
            composite_set.add(num_list[i])
    return composite_set