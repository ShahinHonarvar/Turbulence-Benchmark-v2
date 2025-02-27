def lists_with_product_equal_n(numbers):
    target_product = 74
    n = len(numbers)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length) % n
            product *= numbers[end - 1]
            if product == target_product:
                result.append(numbers[start:end] if start < end else numbers[start:] + numbers[:end])
            elif product > target_product:
                break
        product //= numbers[start]
    return result