def lists_with_product_equal_n(lst):
    target = 54
    results = []
    for i in range(len(lst)):
        curr_product = 1
        for j in range(i, i + len(lst)):
            curr_product *= lst[j % len(lst)]
            if curr_product == target:
                results.append(lst[i:j + 1])
                break
            elif curr_product > target or j == i + len(lst) - 1:
                break
    return results