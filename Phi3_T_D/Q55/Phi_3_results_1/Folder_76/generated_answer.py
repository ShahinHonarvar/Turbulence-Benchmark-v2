def lists_with_product_equal_n(circular_list):
    target_product = 247
    num_elements = len(circular_list)
    circular_list = circular_list + circular_list
    result = []
    for i in range(num_elements):
        for j in range(i + 1, num_elements + 1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == target_product:
                result.append(sublist)
    return result