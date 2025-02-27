def lists_with_product_equal_n(numbers):
    result = []
    n = 85
    size = len(numbers)
    for start in range(size):
        product = 1
        for length in range(1, size + 1):
            index = (start + length - 1) % size
            product *= numbers[index]
            if product == n:
                result.append(numbers[start:start + length])
            elif product > n:
                break
    return result