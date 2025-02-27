def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    npower = 2 ** n
    for x in range(npower):
        sublist = []
        product_so_far = 1
        for i in range(n):
            selected = x >> i & 1
            if selected:
                sublist.append(circular_list[i % n])
                product_so_far *= circular_list[i % n]
                if product_so_far == 32:
                    result.append(sublist.copy())
                    sublist.clear()
                    product_so_far = 1
            elif sublist:
                sublist.clear()
        if sublist and product_so_far == 32:
            result.append(sublist.copy())
            sublist.clear()
            product_so_far = 1
    return result