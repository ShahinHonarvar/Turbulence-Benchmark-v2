def lists_with_product_equal_n(numbers):
    n = -32
    result = []
    length = len(numbers)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= numbers[j % length]
            if product == n:
                result.append(numbers[i:j + 1 % length])
    return result