def composite_nums_between_indices(num_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    composites = {num for num in num_list[:4] if not is_prime(num)}
    return composites