def lists_with_product_equal_n(circular_list, n=-968):
    size = len(circular_list)

    def find_sublists(start):
        product = 1
        sublist = []
        for i in range(size):
            product *= circular_list[(start + i) % size]
            sublist.append(circular_list[(start + i) % size])
            if product == n:
                yield sublist[:]
            if product != n and product != 1:
                sublist.clear()
                product = 1
                start += i + 1
                break
    result = []
    for i in range(size):
        result.extend(find_sublists(i))
    return result