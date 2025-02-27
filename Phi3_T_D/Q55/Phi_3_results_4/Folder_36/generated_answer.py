from itertools import tee

def lists_with_product_equal_n(circular_list):
    n = 714

    def pairs(iterable):
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)
    results = []
    for i in range(len(circular_list)):
        current_list = circular_list[i:] + circular_list[:i]
        for length in range(1, len(current_list) + 1):
            for sublist in (current_list[i:i + length] for i in range(len(current_list) - length + 1)):
                if n == 1:
                    if 1 in sublist:
                        results.append(sublist)
                        break
                else:
                    product = 1
                    for item in sublist:
                        product *= item
                    if product == n:
                        results.append(sublist)
                        break
    return results