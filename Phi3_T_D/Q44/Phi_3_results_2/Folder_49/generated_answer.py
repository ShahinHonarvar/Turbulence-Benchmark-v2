def composite_nums_between_indices(int_list):

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    comps_set = set()
    for i in range(90, min(201, len(int_list))):
        if is_composite(int_list[i]):
            comps_set.add(int_list[i])
    return comps_set