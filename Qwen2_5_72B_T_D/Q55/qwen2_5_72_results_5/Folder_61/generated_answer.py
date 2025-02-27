def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= arr[end % n]
            if product == -10:
                result.append(arr[start:end % n + 1])
            elif abs(product) > 10:
                break
    return result