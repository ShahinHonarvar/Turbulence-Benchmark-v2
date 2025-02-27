def lists_with_product_equal_n(lst):

    def find_sublists_with_product(n, lst):
        sublists = []
        length = len(lst)
        for start in range(length):
            product = 1
            for end in range(start, start + length):
                index = end % length
                product *= lst[index]
                if product == n:
                    sublists.append(lst[start:index + 1])
                elif product > n:
                    break
        return sublists
    return find_sublists_with_product(91, lst)