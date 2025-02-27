def lists_with_product_equal_n(circular_list):
    N = -94
    size = len(circular_list)

    def contiguous_product(lst, start, end):
        product = 1
        for i in range(start, end):
            product *= lst[i % size]
        return product
    result = []
    for length in range(1, size + 1):
        for i in range(size):
            current_product = contiguous_product(circular_list, i, i + length)
            if current_product == N:
                result.append(circular_list[i:i + length] + circular_list[:length % size])
    return result