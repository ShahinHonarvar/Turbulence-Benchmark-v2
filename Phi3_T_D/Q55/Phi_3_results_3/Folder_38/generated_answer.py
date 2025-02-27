def lists_with_product_equal_n(circular_list):
    n = -23
    results = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j % len(circular_list)]
            if 1 not in sublist and all(sublist) != 0 and (n == abs((prod := abs((prod := math.prod(sublist)))))):
                results.append(sublist)
    return results