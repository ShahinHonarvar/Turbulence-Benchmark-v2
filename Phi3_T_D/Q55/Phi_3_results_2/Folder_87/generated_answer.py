def get_product_of_sublist(sublist):
    product = 1
    for num in sublist:
        product *= num
    return product

def rotate_list(lst, n):
    return lst[n:] + lst[:n]

def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    pivot = 0
    for _ in range(n):
        sublist = []
        for _ in range(n):
            sublist.append(circular_list[pivot])
            if get_product_of_sublist(sublist) == 27:
                result.append(sublist.copy())
            pivot = (pivot + 1) % n
        circular_list = rotate_list(circular_list, 1)
    return result