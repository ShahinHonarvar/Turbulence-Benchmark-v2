def lists_with_product_equal_n(circular_list):

    def find_sublists(lst):
        n = len(lst)
        sublists = []
        for start in range(n):
            product = 1
            for end in range(n):
                index = (start + end) % n
                product *= lst[index]
                if product == -18:
                    sublists.append(lst[start:start + end + 1])
        return sublists
    sublists = find_sublists(circular_list)
    return sublists if sublists else []