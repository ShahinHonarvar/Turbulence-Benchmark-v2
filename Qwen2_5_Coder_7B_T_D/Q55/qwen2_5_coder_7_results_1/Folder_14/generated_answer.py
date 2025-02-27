def lists_with_product_equal_n(numbers):
    result = []
    n = len(numbers)
    for i in range(n):
        product = 1
        for j in range(i, (i + n) // 2):
            product *= numbers[j % n]
            if product == -72:
                result.append(numbers[i:j + 1])
                break
            elif product > -72:
                break
    return result