def lists_with_product_equal_n(lst):

    def find_sublists_with_product(lst, n):
        result = []
        for start in range(len(lst)):
            product = 1
            for end in range(start, start + len(lst)):
                product *= lst[end % len(lst)]
                if product == n:
                    result.append(lst[start:end + 1])
                elif product > n:
                    break
        return result
    return find_sublists_with_product(lst, 3)