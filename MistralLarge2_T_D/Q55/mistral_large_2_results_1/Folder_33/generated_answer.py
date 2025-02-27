def lists_with_product_equal_n(circular_list):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            sublist = circular_list[i:j]
            if product(sublist) == -115:
                result.append(sublist)
    return result