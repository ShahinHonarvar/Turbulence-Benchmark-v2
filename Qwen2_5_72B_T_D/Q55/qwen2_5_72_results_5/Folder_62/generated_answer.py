from itertools import islice
    from math import prod

def lists_with_product_equal_n(circular_list):

    def rotate_list(lst, pos):
        return lst[pos:] + lst[:pos]
    found_sublists = []
    for i in range(len(circular_list)):
        rotated = rotate_list(circular_list, i)
        for size in range(1, len(rotated) + 1):
            for j in range(0, len(rotated), size):
                slice = list(islice(rotated, j, j + size))
                if prod(slice) == 100:
                    found_sublists.append(slice)
    return found_sublists