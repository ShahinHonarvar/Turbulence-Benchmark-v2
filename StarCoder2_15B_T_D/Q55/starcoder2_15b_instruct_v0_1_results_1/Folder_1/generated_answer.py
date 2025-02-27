def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        prod = 1
        j = i
        while prod != -51:
            prod *= circular_list[j]
            if prod == -51:
                result.append(circular_list[i:j + 1])
            j = (j + 1) % n
            if prod == 1:
                break
    return result