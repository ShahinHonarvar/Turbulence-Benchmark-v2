def lists_with_product_equal_n(circular_list):
    n = 42
    length = len(circular_list)

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    result = []
    for start in range(length):
        for end in range(start, start + length):
            sublist = [circular_list[i % length] for i in range(start, end + 1)]
            if product(sublist) == n:
                result.append(sublist)
    return result