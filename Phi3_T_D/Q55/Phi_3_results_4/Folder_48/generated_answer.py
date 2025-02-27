def lists_with_product_equal_n(circular_list):
    n, res = (990, [])
    circular_list_len = len(circular_list)
    for i in range(circular_list_len):
        product = 1
        for j in range(i, circular_list_len * 2):
            product *= circular_list[j % circular_list_len]
            if circular_list[j % circular_list_len] == 1 and product < n:
                break
            if product == n:
                res.append(circular_list[i:j + 1])
    return res