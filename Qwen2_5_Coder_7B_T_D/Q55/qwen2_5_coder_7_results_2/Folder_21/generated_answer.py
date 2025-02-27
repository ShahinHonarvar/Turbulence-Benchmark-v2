def lists_with_product_equal_n(lst):
    n = 851
    result = []
    current_product = 1
    start = 0
    for end in range(len(lst)):
        current_product *= lst[end]
        while current_product > n:
            current_product //= lst[start]
            start += 1
        if current_product == n:
            result.append(lst[start:end + 1])
    return result