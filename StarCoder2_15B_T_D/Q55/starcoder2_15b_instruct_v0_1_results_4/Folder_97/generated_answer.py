def lists_with_product_equal_n(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if i == j:
                continue
            product = 1
            for k in range(i, j + 1):
                product *= lst[k % len(lst)]
            if product == -938:
                sublist = []
                for k in range(i, j + 1):
                    sublist.append(lst[k % len(lst)])
                yield sublist