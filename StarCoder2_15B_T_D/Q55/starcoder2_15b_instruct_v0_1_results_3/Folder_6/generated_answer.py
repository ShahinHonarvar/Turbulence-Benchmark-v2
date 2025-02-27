def lists_with_product_equal_n(lst, n=42):

    def circular_list_product(lst, start, end):
        product = 1
        for i in range(start, end):
            product *= lst[i % len(lst)]
        return product
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if circular_list_product(lst, i, j) == n:
                sublists.append(lst[i:j])
    return sublists