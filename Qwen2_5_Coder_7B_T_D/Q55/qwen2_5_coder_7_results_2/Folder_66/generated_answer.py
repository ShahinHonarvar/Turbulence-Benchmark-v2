def lists_with_product_equal_n(lst):

    def find_sublists(start, product):
        if product == 1:
            return [[]]
        if start == len(lst):
            return []
        sublists = []
        temp_product = 1
        for i in range(start, len(lst)):
            temp_product *= lst[i]
            if temp_product == product:
                sublists.append(lst[start:i + 1])
            elif temp_product > product:
                break
        sublists.extend(find_sublists(start + 1, product))
        return sublists
    result = find_sublists(0, 78)
    for i in range(len(lst)):
        result.extend(find_sublists(i + 1, 78))
    return result