def lists_with_product_equal_n(lst, n=-89):
    size = len(lst)
    result = []
    for start in range(size):
        product = 1
        for end in range(size):
            index = (start + end) % size
            product *= lst[index]
            if product == n:
                result.append(lst[start:start + end + 1] if start + end + 1 <= size else lst[start:] + lst[:index + 1])
    return result