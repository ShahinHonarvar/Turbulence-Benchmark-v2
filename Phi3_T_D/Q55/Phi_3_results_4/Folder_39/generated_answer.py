from itertools import cycle

def lists_with_product_equal_n(circular_list):

    def find_sublists_with_product(sublist, target):
        n = len(sublist)
        results = []
        for i in range(1 << n):
            temp = [sublist[j] for j in range(n) if i & 1 << j]
            product = 1
            for elem in temp:
                product *= elem
            if product == target:
                results.append(temp)
        return results
    results = []
    n = len(circular_list)
    for i in range(n):
        for j in find_sublists_with_product(circular_list[i:] + circular_list[:i], -46):
            if j not in results:
                results.append(j)
    return results