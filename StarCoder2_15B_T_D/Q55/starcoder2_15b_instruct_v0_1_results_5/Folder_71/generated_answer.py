def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        window = []
        product = 1
        size = 0
        for j in range(i, i + n):
            window.append(circular_list[j % n])
            product *= circular_list[j % n]
            size += 1
            if product == 47:
                result.append(window[:])
            elif product > 47:
                while product > 47:
                    product /= window[0]
                    window.pop(0)
                    size -= 1
                if product == 47:
                    result.append(window[:])
    return result