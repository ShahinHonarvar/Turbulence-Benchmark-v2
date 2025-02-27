from itertools import islice

def lists_with_product_equal_n(circular_list, n=-16):

    def circular_sublists(lst, length):
        for start in range(len(lst)):
            sublist = list(islice(lst, start, start + length))
            if len(sublist) == length:
                yield sublist
        for start in range(length - len(lst)):
            sublist = list(islice(lst, start)) + list(islice(lst, start + length - len(lst)))
            yield sublist
    result = []
    for length in range(1, len(circular_list) + 1):
        for sublist in circular_sublists(circular_list, length):
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result