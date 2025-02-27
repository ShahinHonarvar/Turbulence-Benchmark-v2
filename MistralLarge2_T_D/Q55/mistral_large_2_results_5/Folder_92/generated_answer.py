def lists_with_product_equal_n(circular_list):

    def find_sublists(lst):
        sublists = []
        for start in range(len(lst)):
            product = 1
            for end in range(start, len(lst)):
                product *= lst[end]
                if product == 5:
                    sublists.append(lst[start:end + 1])
                elif product > 5:
                    break
        return sublists
    return find_sublists(circular_list * 2)