def lists_with_product_equal_n(arr):
    n = -938
    result = []
    for i in range(len(arr)):
        product = 1
        for j in range(i, len(arr) + i):
            product *= arr[j % len(arr)]
            if product == n:
                result.append(arr[i:j % len(arr) + 1])
    return result