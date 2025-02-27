from collections import deque

def lists_with_product_equal_n(circular_list):

    def product_sublists(index, target_product):
        sublists = []
        current_product = 1
        d = deque()
        while index < len(circular_list):
            current_product *= circular_list[index]
            d.append(circular_list[index])
            if current_product == target_product:
                sublists.append(list(d))
            while current_product >= target_product and d:
                current_product /= d.popleft()
            index += 1
        return sublists
    all_sublists = []
    target_product = -18
    n = len(circular_list)
    for start in range(n):
        all_sublists.extend(product_sublists(start, target_product))
        circular_list.append(circular_list.pop(0))
    return all_sublists