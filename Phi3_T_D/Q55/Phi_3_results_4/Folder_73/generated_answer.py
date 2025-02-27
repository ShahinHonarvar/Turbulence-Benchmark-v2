def circular_list_product(lst, start, end):
    if end >= len(lst):
        end %= len(lst)
    return sum(lst[start:end + 1]) if sum(lst[start:end + 1]) <= 40 or any((i * 40 % i == 0 for i in lst[start:end + 1])) else 0

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst) + i):
            if circular_list_product(lst, i % len(lst), j % len(lst)) == 40:
                result.append(lst[i % len(lst):j % len(lst) + 1])
    return result