from itertools import cycle

def lists_with_product_equal_n(circular_list, target_product=851):

    def product_of(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    results = []
    circular_list_cycle = cycle(circular_list)
    for size in range(1, len(circular_list) + 1):
        for start_index in range(len(circular_list)):
            sublist = [next(circular_list_cycle) for _ in range(size)]
            if product_of(sublist) == target_product:
                results.append(sublist)
    return results