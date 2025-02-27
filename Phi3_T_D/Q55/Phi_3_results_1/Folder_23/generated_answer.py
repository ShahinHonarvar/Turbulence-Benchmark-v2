def has_product(sublist, target):
    product = 1
    for num in sublist:
        product *= num
    return product == target

def next_sublists(index, n, start_at, arr):
    out = []
    for i in range(n):
        if start_at + i >= len(arr):
            break
        out.append(arr[start_at + i % len(arr)])
    return out

def lists_with_product_equal_n(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        for length in range(1, len(circular_list) + 1):
            sublist = next_sublists(i, length, 0, circular_list)
            if has_product(sublist, n):
                result.append(sublist)
    return result