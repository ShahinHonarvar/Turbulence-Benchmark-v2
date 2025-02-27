from collections import deque

def lists_with_product_equal_n(circular_list):

    def get_sublists_with_product(lst, target_product):
        sublists = []
        n = len(lst)
        for start in range(n):
            product = 1
            for end in range(start, start + n):
                product *= lst[end % n]
                if product == target_product:
                    sublists.append(lst[start:end % n + 1])
                elif product > target_product:
                    break
        return sublists
    return get_sublists_with_product(circular_list, 54)