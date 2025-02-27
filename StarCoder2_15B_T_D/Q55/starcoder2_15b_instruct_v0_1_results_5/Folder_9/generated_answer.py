def lists_with_product_equal_n(lst):
    n = -36
    result = []
    for i in range(len(lst)):
        current_product = 1
        current_list = []
        for j in range(i, i + len(lst)):
            current_product *= lst[j % len(lst)]
            current_list.append(lst[j % len(lst)])
            if current_product == n:
                result.append(current_list)
            elif current_product == 0:
                break
    return result