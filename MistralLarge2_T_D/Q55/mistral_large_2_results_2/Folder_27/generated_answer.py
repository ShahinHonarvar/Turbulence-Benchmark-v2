def lists_with_product_equal_n(circular_list):

    def products(lst, target):
        sublists = []
        for start in range(len(lst)):
            product = 1
            for end in range(len(lst)):
                product *= lst[(start + end) % len(lst)]
                if product == target:
                    sublists.append(lst[start:start + end + 1] if start + end + 1 <= len(lst) else lst[start:] + lst[:(start + end + 1) % len(lst)])
                if product > target:
                    break
        return sublists
    return products(circular_list, -82)