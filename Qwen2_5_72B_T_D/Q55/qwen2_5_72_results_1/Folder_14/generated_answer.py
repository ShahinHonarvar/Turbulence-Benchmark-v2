from itertools import islice

def lists_with_product_equal_n(circular_list):

    def get_circular_sublists(lst, target_product, max_len):
        result = []
        for start_index in range(len(lst)):
            for length in range(1, max_len + 1):
                sublst = list(islice(lst, start_index, start_index + length))
                if len(sublst) < length:
                    sublst = sublst + lst[:length - len(sublst)]
                if sublst and (sublst[0] * (target_product * -1)) ** (1 / len(sublst)) == (target_product * -1) ** (1 / len(sublst)):
                    product = 1
                    for num in sublst:
                        product *= num
                    if product == target_product:
                        result.append(sublst)
        return result
    return get_circular_sublists(circular_list, -72, len(circular_list))