def lists_with_product_equal_n(numbers):
    n = len(numbers)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            current_index = (start + end) % n
            product *= numbers[current_index]
            if product == -61:
                result.append(numbers[start:current_index + 1])
            if abs(product) > 61:
                break
    return result