def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def check_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == -5
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[j % n:] + circular_list[:j % n]
            if check_product(sublist[:j - i + 1]):
                result.append(sublist[:j - i + 1])
    return result