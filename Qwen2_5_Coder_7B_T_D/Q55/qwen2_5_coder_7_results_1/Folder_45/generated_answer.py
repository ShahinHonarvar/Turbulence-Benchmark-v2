def lists_with_product_equal_n(lst):

    def find_sublists(start, end):
        product = 1
        sublists = []
        for i in range(start, end):
            product *= lst[i]
            if product == -5:
                sublists.append(lst[start:i + 1])
            elif product % -5 == 0:
                for j in range(start, i + 1):
                    if product // lst[j] == -5:
                        sublists.append(lst[j:i + 1])
                        break
        return sublists
    n = len(lst)
    result = []
    for i in range(n):
        result.extend(find_sublists(i, n) + find_sublists(0, i))
    return result