def lists_with_product_equal_n(numbers):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p
    n = len(numbers)
    result = []
    for i in range(n):
        for j in range(1, n):
            sublist = numbers[i:i + j]
            if product(sublist) == -7:
                result.append(sublist)
    return result