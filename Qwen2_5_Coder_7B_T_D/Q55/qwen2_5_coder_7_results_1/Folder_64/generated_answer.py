def lists_with_product_equal_n(numbers):
    result = []
    n = len(numbers)
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            product *= numbers[(start + length - 1) % n]
            if product == 3:
                result.append(numbers[start:start + length])
    return result