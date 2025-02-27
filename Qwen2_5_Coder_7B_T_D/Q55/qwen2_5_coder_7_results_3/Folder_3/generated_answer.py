def lists_with_product_equal_n(lst):

    def find_sublists(start):
        for length in range(1, len(lst) - start + 1):
            product = 1
            for i in range(length):
                product *= lst[(start + i) % len(lst)]
            if product == -22:
                yield [lst[(start + i) % len(lst)] for i in range(length)]
    result = []
    for i in range(len(lst)):
        result.extend(find_sublists(i))
    return result