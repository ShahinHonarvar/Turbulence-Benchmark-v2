def lists_with_product_equal_n(circle):
    n = -30
    result = []
    for size in range(1, len(circle) + 1):
        for start in range(len(circle)):
            current_sum = 1
            for i in range(start, start + size):
                current_sum *= circle[i % len(circle)]
            if current_sum == n:
                result.append(circle[start:start + size])
    return result