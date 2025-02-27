def lists_with_product_equal_n(lst):

    def find_sublists_with_product(lst, target):
        n = len(lst)
        result = []
        for start in range(n):
            product = 1
            for end in range(start, start + n):
                product *= lst[end % n]
                if product == target:
                    result.append(lst[start % n:end % n + 1])
                elif product > target:
                    break
        return result
    return find_sublists_with_product(lst, 91)