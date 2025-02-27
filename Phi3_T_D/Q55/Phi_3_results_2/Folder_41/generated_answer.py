def lists_with_product_equal_n(circular_list):
    temp_list = circular_list + circular_list[0:len(circular_list) - 1]
    results = []
    for i in range(len(temp_list)):
        product = 1
        for j in range(i, len(temp_list)):
            product *= temp_list[j]
            if product == -20:
                results.append(temp_list[i:j + 1])
                break
            if product > -20:
                break
    return results