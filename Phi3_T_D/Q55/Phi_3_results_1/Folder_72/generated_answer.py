def lists_with_product_equal_n(arr, n=10):
    len_arr = len(arr)
    result = []
    for start in range(len_arr):
        product = 1
        for i in range(start, len_arr + start):
            product *= arr[i % len_arr]
            if product == n:
                result.append(arr[start:i % len_arr + 1])
            elif product > n:
                break
    return result