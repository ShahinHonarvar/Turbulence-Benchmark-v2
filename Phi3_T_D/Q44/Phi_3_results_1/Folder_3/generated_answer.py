def composite_nums_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    composite_set = set()
    for i in range(66, 94):
        if not is_prime(lst[i]) and lst[i] > 1:
            composite_set.add(lst[i])
    return composite_set