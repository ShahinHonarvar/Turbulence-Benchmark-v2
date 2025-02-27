def composite_nums_between_indices(lst):
    result_set = set()
    start_index, end_index = (51, 86)

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    for i in range(start_index, end_index + 1):
        if is_composite(lst[i]):
            result_set.add(lst[i])
    return result_set