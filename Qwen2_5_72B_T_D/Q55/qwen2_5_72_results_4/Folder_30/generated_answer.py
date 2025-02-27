from itertools import cycle

def lists_with_product_equal_n(circular_list):

    def product_sublists(lst, target_product):
        n = len(lst)
        result = []
        for start in range(n):
            product = 1
            for i, num in enumerate(cycle(lst[start:])):
                if i > n:
                    break
                product *= num
                if product == target_product:
                    result.append(lst[start:start + i + 1])
                if product > target_product:
                    break
        return result
    return product_sublists(circular_list, 99)