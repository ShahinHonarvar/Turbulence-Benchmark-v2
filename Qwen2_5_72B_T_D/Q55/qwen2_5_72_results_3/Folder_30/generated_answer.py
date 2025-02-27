def lists_with_product_equal_n(arr):
    n = len(arr)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            real_end = (start + end) % n
            product *= arr[real_end]
            if product == 99:
                result.append(arr[start:real_end + 1])
            if product > 99:
                break
    return result