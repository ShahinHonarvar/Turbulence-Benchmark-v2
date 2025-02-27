def lists_with_product_equal_n(lst):

    def find_sublists(start):
        product = 1
        sublists = []
        for i in range(start, len(lst)):
            product *= lst[i]
            if product == -69:
                sublists.append(lst[start:i + 1])
            elif product > -69:
                break
        return sublists
    result = []
    for i in range(len(lst)):
        result.extend(find_sublists(i))
        result.extend(find_sublists(i + 1))
    return result