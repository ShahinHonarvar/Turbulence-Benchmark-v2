def lists_with_product_equal_n(circular_list):
    N = -83
    n = len(circular_list)
    circular_list = circular_list + circular_list[:-1]
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, n):
            product *= circular_list[j % n]
            if product == N:
                result.append(circular_list[i:j + 1])
            elif product > N:
                break
            sublist.append(circular_list[j])
    return result