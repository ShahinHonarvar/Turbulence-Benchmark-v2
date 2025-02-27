def lists_with_product_equal_n(numbers):
    target_product = -82
    n = len(numbers)
    result = []
    for size in range(1, n + 1):
        for start in range(n):
            product = 1
            for i in range(start, start + size):
                product *= numbers[i % n]
            if product == target_product:
                result.append(numbers[start:start + size])
                if size > 1 and start + size > n:
                    result.append(numbers[start:] + numbers[:start + size - n])
    return result