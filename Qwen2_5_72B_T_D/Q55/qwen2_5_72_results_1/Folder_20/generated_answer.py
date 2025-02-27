def lists_with_product_equal_n(circular_list):

    def get_sublists(start, n):
        sublists = []
        product = 1
        for i in range(start, start + len(circular_list)):
            index = i % len(circular_list)
            product *= circular_list[index]
            if product == -69:
                sublists.append(circular_list[start:index + 1])
            elif abs(product) > 69:
                break
        return sublists
    result = []
    for i in range(len(circular_list)):
        result.extend(get_sublists(i, -69))
    return result