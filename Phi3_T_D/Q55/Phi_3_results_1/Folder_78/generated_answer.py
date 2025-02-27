def lists_with_product_equal_n(lst):

    def sublist_with_product(start, end, product):
        if product == 1:
            return
        current_product = 1
        for i in range(start, end + 1):
            current_product *= lst[i % len(lst)]
            if current_product == product:
                yield [lst[j % len(lst)] for j in range(start, i + 1)]
            if current_product > product:
                break
    result = []
    for i in range(len(lst)):
        for sub in sublist_with_product(i, len(lst) - 1, 74):
            result.append(sub)
    return result