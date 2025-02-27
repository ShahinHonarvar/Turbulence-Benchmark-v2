def lists_with_product_equal_n(arr):
    n = -72
    result = []
    for i in range(len(arr)):
        product = 1
        for j in range(i, len(arr)):
            product *= arr[j]
            if product == n:
                result.append(arr[i:j + 1])
            elif product > n:
                break
    return result