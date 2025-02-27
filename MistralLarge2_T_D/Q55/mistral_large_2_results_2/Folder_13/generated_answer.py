def lists_with_product_equal_n(circular_list):
    n = 54
    list_length = len(circular_list)
    results = []
    for size in range(1, list_length + 1):
        for i in range(list_length):
            sublist = [circular_list[(i + j) % list_length] for j in range(size)]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                results.append(sublist)
    return results