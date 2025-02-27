from functools import reduce
        from operator import mul

def lists_with_product_equal_n(circular_list):

    def get_continuous_sublists(lst):
        return [lst[i:j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1)] + [lst[-1:] + lst[:1]]

    def check_sublist_product(sublist):
        return reduce(mul, sublist, 1) == -94
    result = []
    for _ in range(len(circular_list)):
        continuous_sublists = get_continuous_sublists(circular_list)
        for sublist in continuous_sublists:
            if check_sublist_product(sublist):
                result.append(sublist)
        circular_list = circular_list[-1:] + circular_list[:-1]
    return result