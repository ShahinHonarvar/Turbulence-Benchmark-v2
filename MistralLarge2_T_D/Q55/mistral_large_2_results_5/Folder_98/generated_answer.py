def lists_with_product_equal_n(circular_list):

    def extend_list(lst, n):
        return lst * n

    def find_sublists(lst):
        sublists = []
        n = len(lst)
        extended_list = extend_list(lst, 2)
        for i in range(n):
            product = 1
            for j in range(i, i + n):
                product *= extended_list[j]
                if product == -1:
                    sublists.append(extended_list[i:j + 1])
        return sublists
    result = find_sublists(circular_list)
    return result if result else []