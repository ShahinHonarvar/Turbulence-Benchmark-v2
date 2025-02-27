def lists_with_product_equal_n(circular_list):

    def find_sublists(circular_list, start, n):
        length = len(circular_list)
        sublists = []
        for size in range(1, length + 1):
            for i in range(start, start + length):
                sublist = circular_list[i:i + size]
                if len(sublist) == size and product(sublist) == n:
                    sublists.append(sublist)
        return sublists

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    length = len(circular_list)
    circular_list = circular_list * 2
    result = []
    for i in range(length):
        result.extend(find_sublists(circular_list, i, -75))
    return result