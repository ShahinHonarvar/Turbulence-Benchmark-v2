def lists_with_product_equal_n(circular_list):
    n = -76
    result = []
    circular_list_length = len(circular_list)
    for i in range(circular_list_length):
        product = 1
        j = i
        while product != n and (j > 0 and circular_list[j - 1] * circular_list[j]):
            product *= circular_list[j]
            j = (j + 1) % circular_list_length
            if product == n:
                sublist = circular_list[i:j] if i != j else circular_list[i:j + 1]
                result.append(sublist)
                break
    return result