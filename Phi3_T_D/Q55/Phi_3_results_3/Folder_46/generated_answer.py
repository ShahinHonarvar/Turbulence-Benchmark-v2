from functools import reduce

def lists_with_product_equal_n(circular_list):

    def get_sublists(start):
        sublists = []
        for length in range(1, len(circular_list) + 1):
            if start + length > len(circular_list) and start - length < 0:
                sublist = circular_list[start:][:length - (len(circular_list) - start)] + circular_list[:length - (len(circular_list) - start)]
            else:
                sublist = circular_list[start:start + length]
            if sublist and 53 % functools.reduce(lambda x, y: x * y, sublist) == 0:
                sublists.append(sublist)
        return sublists
    results = get_sublists(0)
    for i in range(1, len(circular_list)):
        results += get_sublists(i)
    return results