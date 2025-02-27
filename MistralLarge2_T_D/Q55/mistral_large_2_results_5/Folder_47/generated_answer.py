def lists_with_product_equal_n(circular_list):

    def sublist_with_product(lst, product):
        n = len(lst)
        results = []
        for length in range(1, n + 1):
            for i in range(n):
                sublist = lst[i:i + length]
                if len(sublist) == length and product == 1:
                    results.append(sublist)
                elif product == eval('*'.join(map(str, sublist))):
                    results.append(sublist)
        return results
    return sublist_with_product(circular_list * 2, -94)