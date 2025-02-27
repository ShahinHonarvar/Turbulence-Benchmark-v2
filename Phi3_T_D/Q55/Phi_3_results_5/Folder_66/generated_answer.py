def lists_with_product_equal_n(circular):
    N = 78
    result = []
    for i in range(len(circular)):
        for j in range(i, len(circular) + i):
            sublist = circular[i:j % len(circular)]
            if len(sublist) < len(circular) and sublist[0] * sublist[1] == N:
                product = 1
                for num in sublist:
                    product *= num
                if product == N:
                    result.append(sublist)
    return result