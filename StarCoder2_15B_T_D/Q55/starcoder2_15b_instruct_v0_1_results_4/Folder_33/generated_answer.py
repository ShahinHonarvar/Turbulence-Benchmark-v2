def lists_with_product_equal_n(list_with_n):
    result = []
    for i in range(len(list_with_n)):
        product = 1
        window = []
        for j in range(i, i + len(list_with_n)):
            window.append(list_with_n[j % len(list_with_n)])
            product *= list_with_n[j % len(list_with_n)]
            if product == -115:
                result.append(window.copy())
    return result