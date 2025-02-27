def lists_with_product_equal_n(lst, n=-54):
    length = len(lst)
    result = []
    for start in range(length):
        product = 1
        for end in range(length):
            product *= lst[(start + end) % length]
            if product == n:
                result.append(lst[start:start + end + 1] + lst[:start + end + 1 - length])
                break
    return result