def circular_index(index, size):
    return index % size

def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    target_product = -83
    results = []
    for i in range(size):
        for j in range(i + 1, size + i):
            sublist = circular_list[circular_index(i, size):circular_index(j, size)]
            product = 1
            for num in sublist:
                product *= num
            if product == target_product:
                results.append(sublist)
    return results