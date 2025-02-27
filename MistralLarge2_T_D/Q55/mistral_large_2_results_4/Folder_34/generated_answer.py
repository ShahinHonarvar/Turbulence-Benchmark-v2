def lists_with_product_equal_n(lst):

    def sublists(lst, n):
        results = []
        for i in range(len(lst)):
            product = 1
            for j in range(i, len(lst)):
                product *= lst[j]
                if product == n:
                    results.append(lst[i:j + 1])
                elif product > n:
                    break
            if i > 0 and lst[i - 1] * product == n:
                results.append(lst[i - 1:] + lst[:i])
        return results
    return sublists(lst * 2, -81)