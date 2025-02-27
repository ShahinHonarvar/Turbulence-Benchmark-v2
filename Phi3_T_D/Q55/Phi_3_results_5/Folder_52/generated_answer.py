def lists_with_product_equal_n(lst):
    product = 37
    results = []
    n = len(lst)
    for size in range(1, n + 1):
        for start in range(n):
            temp = lst[start:start + size]
            full_list = temp + lst[0:size - (n - start)]
            if temp == []:
                break
            if size == n:
                temp = full_list
            if all((x != 0 for x in temp)) and product == prod(temp):
                results.append(temp)
    return results