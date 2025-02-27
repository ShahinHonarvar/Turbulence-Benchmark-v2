def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target = 49
    contiguous_sublists = []
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1] + circular_list[0:j + 1 - n]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == target:
                contiguous_sublists.append(sublist)
    return contiguous_sublists