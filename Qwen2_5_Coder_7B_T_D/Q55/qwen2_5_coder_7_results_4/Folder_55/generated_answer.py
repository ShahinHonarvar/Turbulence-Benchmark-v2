def lists_with_product_equal_n(numbers):
    n = -6
    result = []
    length = len(numbers)
    for i in range(length):
        product = 1
        for j in range(i, length + i):
            product *= numbers[j % length]
            if product == n:
                result.append(numbers[i:j % length + 1])
            elif product > n:
                break
    return result