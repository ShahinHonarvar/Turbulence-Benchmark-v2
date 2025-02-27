def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for start in range(n):
            sublist = [lst[(start + i) % n] for i in range(size)]
            if sublist and all((isinstance(x, int) for x in sublist)):
                product = 1
                for num in sublist:
                    product *= num
                if product == -89:
                    result.append(sublist)
    return result