def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(1, n + 1):
            window = circular_list[i:i + j]
            if len(window) > n:
                break
            product = 1
            for num in window:
                product *= num
            if product == 10:
                result.append(window)
    return result