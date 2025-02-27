def is_composite(n):
    return any((n % i == 0 for i in range(2, int(n ** 0.5) + 1))) and n > 1

def composite_nums_between_indices(int_list):
    return set(filter(is_composite, int_list[40:81]))