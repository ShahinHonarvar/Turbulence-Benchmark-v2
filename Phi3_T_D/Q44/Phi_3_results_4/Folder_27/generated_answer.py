def composite_nums_between_indices(int_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_composite(n):
        return not is_prime(n)
    return {num for num in int_list[22:64] if is_composite(num)}