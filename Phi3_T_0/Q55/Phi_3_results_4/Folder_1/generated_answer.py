def lists_with_product_equal_n(circular_list):
    n = -51
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j % len(circular_list)]
            if len(sublist) > 0 and n % sublist[0] == 0:
                temp_n = n
                for num in sublist:
                    if num == 0:
                        break
                    temp_n //= num
                if temp_n == 1:
                    result.append(sublist)
    return result