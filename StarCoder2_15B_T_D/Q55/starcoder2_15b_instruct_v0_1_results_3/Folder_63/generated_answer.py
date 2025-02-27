def lists_with_product_equal_n(circular_list, n):
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i):
            sublist = circular_list[i:j]
            if len(sublist) == len(circular_list):
                sublist = circular_list[i:] + circular_list[:j % len(circular_list)]
            if len(sublist) > 0 and len(sublist) <= len(circular_list) and (product(sublist) == n):
                sublists.append(sublist)
    return sublists

def product(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result