def composite_nums_between_indices(int_list):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {num for idx, num in enumerate(int_list[246:751], start=246) if is_composite(num)}