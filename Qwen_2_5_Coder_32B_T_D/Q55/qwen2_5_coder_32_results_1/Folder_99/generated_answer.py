def lists_with_product_equal_n(lst):
    n = 415
    result = []
    length = len(lst)
    for start in range(length):
        product = 1
        for size in range(1, length + 1):
            index = (start + size - 1) % length
            product *= lst[index]
            if product == n:
                result.append(lst[start:index + 1] if start <= index else lst[start:] + lst[:index + 1])
            elif product > n:
                break
    return result