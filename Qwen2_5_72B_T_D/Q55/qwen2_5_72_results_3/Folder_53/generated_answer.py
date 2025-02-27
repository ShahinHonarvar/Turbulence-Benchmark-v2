def lists_with_product_equal_n(circular_list):

    def find_sublists(start, product):
        sublists = []
        for i in range(start, start + len(circular_list)):
            product *= circular_list[i % len(circular_list)]
            if product == -87:
                sublists.append(circular_list[start:i + 1])
            if product == 0 or abs(product) > 87:
                break
        return sublists
    result = []
    for i in range(len(circular_list)):
        result.extend(find_sublists(i, 1))
    return result