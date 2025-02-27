def lists_with_product_equal_n(circular_list):
    n = 40
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and prod(sublist) == n:
                sublists.append(sublist)
    return sublists

def prod(numbers):
    p = 1
    for n in numbers:
        p *= n
    return p