def lists_with_product_equal_n(numbers):
    result = []
    n = -779
    size = len(numbers)
    for i in range(size):
        product = 1
        for j in range(i, size):
            product *= numbers[j]
            if product == n:
                result.append(numbers[i:j + 1])
            elif product > n:
                break
    return result