def lists_with_product_equal_n(numbers):
    result = []
    n = 74
    length = len(numbers)
    for i in range(length):
        product = 1
        for j in range(i, length):
            product *= numbers[j]
            if product == n:
                result.append(numbers[i:j + 1])
            elif product > n:
                break
    return result