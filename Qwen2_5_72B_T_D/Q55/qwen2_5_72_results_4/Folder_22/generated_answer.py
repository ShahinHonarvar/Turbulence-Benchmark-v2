def lists_with_product_equal_n(circular_list):

    def get_sublists(start, product):
        sublists = []
        for size in range(1, len(circular_list) + 1):
            end = (start + size) % len(circular_list)
            current_product = product
            for i in range(start, end):
                current_product *= circular_list[i % len(circular_list)]
            if current_product == 4:
                sublists.append(circular_list[start:end])
            if end <= start:
                break
        return sublists
    result = []
    for i in range(len(circular_list)):
        result.extend(get_sublists(i, 1))
    return result