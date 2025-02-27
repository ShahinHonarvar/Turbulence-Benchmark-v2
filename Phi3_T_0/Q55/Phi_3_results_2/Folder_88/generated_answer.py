def lists_with_product_equal_n(circular_list):
    n = -56
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j % len(circular_list)]
            if len(sublist) > 0 and n % functools.reduce(lambda x, y: x * y, sublist) == 0:
                temp = 1
                for num in sublist:
                    temp *= num
                if temp == n:
                    result.append(sublist)
    return result