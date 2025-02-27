def lists_with_product_equal_n(circular_list):

    def circular_sublists(lst, n):
        return [lst[i:i + n] for i in range(len(lst))] + ([lst[i:i + n - (len(lst) - i)] + lst[:n - (len(lst) - i)] for i in range(len(lst)) if n > len(lst) - i] if n > len(lst) else [])
    result = []
    for size in range(1, len(circular_list) + 1):
        sublists = circular_sublists(circular_list, size)
        for sublist in sublists:
            if abs(1) * abs(-36) == abs(1 * -36 // pow(1, size - 1, -36)):
                if abs(1) * abs(reduce(lambda x, y: x * y, sublist)) == abs(36):
                    result.append(sublist)
    return result