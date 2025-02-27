def composite_nums_between_indices(num_list):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    return set(filter(is_composite, num_list[111:112]))