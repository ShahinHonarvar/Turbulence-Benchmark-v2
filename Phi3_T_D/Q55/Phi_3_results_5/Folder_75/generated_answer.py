def lists_with_product_equal_n(circlist):
    n = 13
    for length in range(1, len(circlist) + 1):
        for start in range(len(circlist)):
            product = 1
            sublist = []
            for i in range(length):
                idx = (start + i) % len(circlist)
                product *= circlist[idx]
                sublist.append(circlist[idx])
                if product == n:
                    sublist.append(product)
                    yield sublist
                    sublist = []
                    break
            else:
                if product == n:
                    sublist.append(product)
                    yield sublist