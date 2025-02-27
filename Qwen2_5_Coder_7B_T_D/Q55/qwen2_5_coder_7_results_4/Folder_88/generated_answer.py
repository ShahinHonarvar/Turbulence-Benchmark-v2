def lists_with_product_equal_n(arr):
    n = len(arr)
    target = -56
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= arr[j % n]
            if product == target:
                result.append(arr[i:j % n + 1])
    return result