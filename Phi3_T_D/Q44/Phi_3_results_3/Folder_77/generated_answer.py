def composite_nums_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    composite_set = {num for num in lst[667:775] if not is_prime(num)}
    return composite_set