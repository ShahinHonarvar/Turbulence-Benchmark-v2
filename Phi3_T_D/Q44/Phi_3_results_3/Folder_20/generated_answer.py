def composite_nums_between_indices(num_list):
    composite_set = set()

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    for i in range(74, min(96, len(num_list))):
        if is_composite(num_list[i]):
            composite_set.add(num_list[i])
    return composite_set