def lists_with_product_equal_n(lst):

    def sublists_with_product(lst, target, start=0):
        if target == 1:
            return [[]]
        if start >= len(lst):
            return []
        result = []
        for end in range(start + 1, len(lst) + 1):
            product = 1
            for i in range(start, end):
                product *= lst[i % len(lst)]
                if product == target:
                    result.append(lst[start:end])
        return result
    return sublists_with_product(lst, 47)