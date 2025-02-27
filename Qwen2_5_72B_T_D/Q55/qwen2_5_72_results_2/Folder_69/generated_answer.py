def lists_with_product_equal_n(numbers):
    n = len(numbers)
    results = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            end = (start + size) % n
            product *= numbers[end - 1]
            if product == 90:
                results.append(numbers[start:end] if start < end else numbers[start:] + numbers[:end])
            if product > 90:
                break
    return results