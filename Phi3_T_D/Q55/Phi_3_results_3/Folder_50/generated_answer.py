def lists_with_product_equal_n(circular_list):
    n = 45
    size = len(circular_list)
    result = []
    for length in range(1, size + 1):
        for start in range(size):
            temp = [circular_list[(start + i) % size] for i in range(length)]
            if prod(temp) == n:
                result.append(temp)
    return result

def prod(lst):
    product = 1
    for num in lst:
        product *= num
    return product