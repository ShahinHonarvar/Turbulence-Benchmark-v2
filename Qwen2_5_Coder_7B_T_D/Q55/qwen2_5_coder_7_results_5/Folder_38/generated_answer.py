def lists_with_product_equal_n(arr):
    n = -23
    result = []
    length = len(arr)
    for i in range(length):
        product = 1
        for j in range(i, length):
            product *= arr[j]
            if product == n:
                result.append(arr[i:j + 1])
            elif product > n:
                break
    return result