def lists_with_product_equal_n(circular_list):
    target_product = 99
    result = []

    def get_products(start, end):
        product = 1
        for i in range(start, end + 1):
            product *= circular_list[i % len(circular_list)]
            if product > target_product:
                break
            elif product == target_product and end - start + 1 <= len(circular_list):
                result.append(circular_list[start:end + 1])
    for i in range(len(circular_list)):
        get_products(i, i)
        get_products(i, i + 1)
        get_products(i, i + 2)
    return result