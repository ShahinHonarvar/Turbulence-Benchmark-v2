def lists_with_product_equal_n(circular_list):
    n = -44
    return [circular_list[i:j] for i in range(len(circular_list)) for j in range(i + 1, len(circular_list) + 1) if all((x != 0 and abs(n) % x == 0 for x in circular_list[i:j])) and n % (prod(circular_list[i:j]) == n)]

def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result