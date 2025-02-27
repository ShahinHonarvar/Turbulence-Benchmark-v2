def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        window = [circular_list[i]]
        product = circular_list[i]
        j = (i + 1) % n
        while product != -57 and j != i:
            window.append(circular_list[j])
            product *= circular_list[j]
            if product > -57:
                product /= window.pop(0)
            else:
                product /= circular_list[j]
            j = (j + 1) % n
        if product == -57:
            result.append(window)
    return result