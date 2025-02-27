from itertools import cycle

def lists_with_product_equal_n(circular_list):
    target = 33
    results = []
    i = 0
    for k in range(1, len(circular_list) + 1):
        for start in range(len(circular_list)):
            product = 1
            sublist = []
            for _ in range(k):
                product *= circular_list[(start + i) % len(circular_list)]
                sublist.append(circular_list[(start + i) % len(circular_list)])
                if len(sublist) == len(circular_list):
                    i += 1
                if product == target:
                    results.append(sublist[:-1])
                    break
                elif product > target:
                    i = 0
                    break
            if product == target:
                break
    return results