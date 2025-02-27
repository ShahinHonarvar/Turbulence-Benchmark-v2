def lists_with_product_equal_n(lst):

    def find_sublists(start):
        product = 1
        sublist = []
        for i in range(len(lst)):
            product *= lst[(start + i) % len(lst)]
            sublist.append(lst[(start + i) % len(lst)])
            if product == 2:
                result.append(sublist[:])
            if product > 2 or (product == 2 and len(sublist) == len(lst)):
                break
            if product == 0:
                sublist = []
                product = 1
    result = []
    for i in range(len(lst)):
        find_sublists(i)
    return result