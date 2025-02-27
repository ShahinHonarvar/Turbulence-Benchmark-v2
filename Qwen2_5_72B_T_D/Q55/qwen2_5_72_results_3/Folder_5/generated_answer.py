from math import prod

def lists_with_product_equal_n(circular_list):

    def get_sublists_with_product(lst, target_product):
        sublists = []
        n = len(lst)
        for start in range(n):
            for end in range(1, n + 1):
                sublist = lst[start:start + end] if start + end <= n else lst[start:] + lst[:end - (n - start)]
                if len(sublist) > 0 and all((isinstance(x, int) for x in sublist)) and (abs(prod(sublist)) == abs(target_product)) and ((target_product < 0) == (prod(sublist) < 0)):
                    sublists.append(sublist)
        return sublists
    all_sublists = get_sublists_with_product(circular_list, -33)
    return all_sublists