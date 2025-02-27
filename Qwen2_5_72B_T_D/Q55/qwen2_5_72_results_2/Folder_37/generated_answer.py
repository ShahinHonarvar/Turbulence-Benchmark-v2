def lists_with_product_equal_n(circular_list):

    def sublists_with_product(lst, target):
        n = len(lst)
        sublists = []
        for start in range(n):
            product = 1
            for end in range(start, start + n):
                product *= lst[end % n]
                if product == target:
                    sublists.append(lst[start:end % n + 1])
                elif product < target:
                    continue
                else:
                    break
        return sublists
    all_sublists = sublists_with_product(circular_list, -76)
    return all_sublists