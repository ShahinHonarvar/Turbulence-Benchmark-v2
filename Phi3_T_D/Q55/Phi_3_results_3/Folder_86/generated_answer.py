def lists_with_product_equal_n(circle):
    n = -779
    res = []
    for i in range(len(circle)):
        product = 1
        temp_list = []
        for j in range(i, i + len(circle)):
            product *= circle[j % len(circle)]
            temp_list.append(circle[j % len(circle)])
            if product == n:
                res.append(temp_list.copy())
            if product > n or j + 1 == i + len(circle):
                break
    return res