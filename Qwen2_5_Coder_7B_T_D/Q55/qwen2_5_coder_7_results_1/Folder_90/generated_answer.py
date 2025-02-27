def lists_with_product_equal_n(l):

    def sublists_with_product(l, n, product=1, start=0, current=[]):
        if product == n:
            return [current]
        if product != 0:
            for i in range(start, len(l)):
                result = sublists_with_product(l, n, product * l[i], i + 1, current + [l[i]])
                if result:
                    return result
        return []
    result = sublists_with_product(l, -690)
    result.extend(sublists_with_product(l[::-1], -690))
    return result