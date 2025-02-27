def lists_with_product_equal_n(circular_list):
    n = -93
    circular_list = circular_list + circular_list[0:1]
    output_list = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        for j in range(i + 1, len(circular_list)):
            product *= circular_list[j]
            if product == n:
                output_list.append(circular_list[i:j + 1])
            elif product < n:
                break
    return output_list