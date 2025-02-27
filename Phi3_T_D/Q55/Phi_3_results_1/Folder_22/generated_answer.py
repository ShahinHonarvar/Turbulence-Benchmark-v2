def circular_product_sublists(circular_list, target=4):

    def get_sub_products(start, end):
        product = 1
        for index in range(start, end + 1):
            product *= circular_list[index % len(circular_list)]
        return product
    result = []
    list_length = len(circular_list)
    for start in range(list_length):
        for length in range(1, list_length + 1):
            end = (start + length - 1) % list_length
            if get_sub_products(start, end) == target:
                result.append(circular_list[start:end + 1])
    return result

def lists_with_product_equal_n(circular_list):
    return circular_product_sublists(circular_list, 4)