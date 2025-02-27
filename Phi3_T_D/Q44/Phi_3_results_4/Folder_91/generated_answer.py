def composite_nums_between_indices(int_list):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {item for item in int_list[5:6] if is_composite(item)}