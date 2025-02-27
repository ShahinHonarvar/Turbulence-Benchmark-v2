def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            sublist = [lst[(i + k) % n] for k in range(j)]
            if 0 in sublist:
                product = 1
                for num in sublist:
                    product *= num
                    if product == 0:
                        result.append(sublist)
                        break
    return result