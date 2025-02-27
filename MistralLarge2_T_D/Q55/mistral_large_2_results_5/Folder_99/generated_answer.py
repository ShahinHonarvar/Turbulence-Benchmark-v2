def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            index = (start + end) % n
            product *= lst[index]
            if product == 415:
                result.append(lst[start:start + end + 1] if start + end + 1 <= n else lst[start:] + lst[:index + 1])
            elif product > 415:
                break
    return result