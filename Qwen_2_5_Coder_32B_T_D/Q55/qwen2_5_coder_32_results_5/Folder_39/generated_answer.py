def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= arr[j % n]
            if product == -46:
                result.append(arr[i:j % n + 1])
    return result