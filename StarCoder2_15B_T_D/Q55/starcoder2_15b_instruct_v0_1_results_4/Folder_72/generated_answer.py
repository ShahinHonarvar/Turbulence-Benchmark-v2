def lists_with_product_equal_n(lst, n=10):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i < j and lst[i:j] and (n == 1):
                result.append(lst[i:j])
    return result