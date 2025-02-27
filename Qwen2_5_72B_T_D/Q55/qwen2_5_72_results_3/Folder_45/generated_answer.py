from itertools import islice

def lists_with_product_equal_n(circular_list):

    def get_sublists_with_product_n(lst, n):
        results = []
        for start_idx in range(len(lst)):
            for size in range(1, len(lst) + 1):
                sublist = list(islice(lst, start_idx, start_idx + size))
                if len(sublist) == size:
                    product = 1
                    for num in sublist:
                        product *= num
                    if product == n:
                        results.append(sublist)
        return results
    n = -5
    results = get_sublists_with_product_n(circular_list, n)
    return results