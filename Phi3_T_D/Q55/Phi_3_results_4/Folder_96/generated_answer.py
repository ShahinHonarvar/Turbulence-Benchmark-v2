def lists_with_product_equal_n(circular_list):

    def get_sublist_products(index):
        product = 1
        sublist = []
        for i in range(index, len(circular_list) + index):
            value = circular_list[i % len(circular_list)]
            if value == 0:
                if product % 10 == 0:
                    return (True, sublist)
            sublist.append(value)
            product *= value
            if product == 0:
                return (True, sublist)
        return (False, [])
    results = []
    for i in range(len(circular_list)):
        found, sublist = get_sublist_products(i)
        if found:
            results.append(sublist)
        else:
            found, sublist = get_sublist_products(i + 1)
            if found:
                results.append(sublist)
    return results