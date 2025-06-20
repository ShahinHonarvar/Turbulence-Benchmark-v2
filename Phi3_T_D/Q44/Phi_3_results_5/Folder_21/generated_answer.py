def composite_nums_between_indices(lst):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    composite_set = set()
    for i in range(262, 747):
        if not is_prime(lst[i]):
            composite_set.add(lst[i])
    return composite_set