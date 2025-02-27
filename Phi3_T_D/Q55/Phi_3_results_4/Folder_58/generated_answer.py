def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            window = circular_list[i:j % len(circular_list)]
            product = 1
            for num in window:
                product *= num
            if product == 733:
                result.append(window)
    return result