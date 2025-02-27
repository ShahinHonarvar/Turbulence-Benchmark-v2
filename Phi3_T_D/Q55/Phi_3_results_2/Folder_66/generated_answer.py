from itertools import cycle

def lists_with_product_equal_n(circular_list):
    n = 78
    result = []
    circles = zip(circular_list, cycle(circular_list))

    def find_sublists(start, current_product, path):
        if current_product == n:
            result.append(path)
            return
        for i, (val, next_val) in enumerate(circles):
            if val == next_val:
                break
            if current_product == 0 or val == 0:
                continue
            if current_product * val == n:
                find_sublists(i + 1, val, path + [val])
            elif current_product * val < n:
                find_sublists(i + 1, current_product * val, path + [val])
    find_sublists(0, 1, [])
    return result