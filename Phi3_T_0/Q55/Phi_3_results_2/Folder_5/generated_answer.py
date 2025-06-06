def lists_with_product_equal_n(circular_list):
    n = -33
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j % len(circular_list)]
            if len(sublist) > 0 and n % sublist[0] == 0:
                temp = n
                for num in sublist:
                    if temp % num == 0:
                        temp //= num
                    else:
                        break
                else:
                    result.append(sublist)
    return result