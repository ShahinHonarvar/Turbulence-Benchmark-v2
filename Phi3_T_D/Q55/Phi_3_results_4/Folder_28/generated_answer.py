def lists_with_product_equal_n(circular_list):
    target = 85
    result = []
    n = len(circular_list)
    for length in range(1, n + 1):
        for i in range(n):
            product = 1
            for j in range(length):
                index = (i + j) % n
                product *= circular_list[index]
                if product > target:
                    break
            if product == target:
                result.append(circular_list[i:i + length])
    return result