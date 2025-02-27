def lists_with_product_equal_n(circular_list, n=-20):

    def sublists_with_product(lst, target):
        result = []
        for start in range(len(lst)):
            product = 1
            for end in range(start, len(lst)):
                product *= lst[end]
                if product == target:
                    result.append(lst[start:end + 1])
                elif product == 0:
                    break
        return result
    extended_list = circular_list * 2
    sublists = sublists_with_product(extended_list, n)
    unique_sublists = [sublist for sublist in sublists if len(sublist) <= len(circular_list)]
    return unique_sublists