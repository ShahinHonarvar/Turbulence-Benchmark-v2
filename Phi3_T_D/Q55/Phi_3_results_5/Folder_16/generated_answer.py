def lists_with_product_equal_n(circular_list, target_product=-837):
    result = []
    list_size = len(circular_list)

    def check_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == target_product
    for i in range(list_size):
        for j in range(i, list_size):
            if check_product(circular_list[i:j + 1]):
                result.append(circular_list[i:j + 1])
    return result