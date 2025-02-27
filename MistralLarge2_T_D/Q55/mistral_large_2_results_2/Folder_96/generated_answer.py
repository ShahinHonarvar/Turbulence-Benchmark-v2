def lists_with_product_equal_n(circular_list):

    def find_sublists_with_product_zero(lst, start):
        n = len(lst)
        sublists = []
        for i in range(n):
            product = 1
            sublist = []
            for j in range(start, start + n):
                index = j % n
                product *= lst[index]
                sublist.append(lst[index])
                if product == 0:
                    sublists.append(sublist[:])
                    sublist = []
                    product = 1
        return sublists
    n = len(circular_list)
    result = []
    for i in range(n):
        result.extend(find_sublists_with_product_zero(circular_list, i))
    return result