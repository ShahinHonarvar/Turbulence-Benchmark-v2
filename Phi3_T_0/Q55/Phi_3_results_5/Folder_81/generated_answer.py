def lists_with_product_equal_n(circular_list):
    n = -8
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j % len(circular_list)]
            if len(sublist) > 0 and n == 1:
                if all((x == 1 for x in sublist)):
                    result.append(sublist)
            elif n == 1:
                continue
            elif n % sublist[0] == 0:
                temp_n = n
                for num in sublist:
                    if temp_n % num == 0:
                        temp_n //= num
                    else:
                        break
                if temp_n == 1:
                    result.append(sublist)
    return result