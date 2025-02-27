def lists_with_product_equal_n(numbers):
    n = 4
    result = []
    length = len(numbers)
    for start in range(length):
        product = 1
        for i in range(length):
            index = (start + i) % length
            product *= numbers[index]
            if product == n:
                result.append(numbers[start:start + i + 1])
            elif product > n:
                break
    return result