from itertools import cycle, islice

def lists_with_product_equal_n(circular_list):
    product = 537
    result = []

    def is_product_n(sublist):
        p = 1
        for n in sublist:
            p *= n
        return p == product
    for size in range(1, len(circular_list) + 1):
        circular_iter = cycle(circular_list)
        for _ in range(len(circular_list)):
            sublist = list(islice(circular_iter, size))
            if is_product_n(sublist) and sublist not in result:
                result.append(sublist)
    return result