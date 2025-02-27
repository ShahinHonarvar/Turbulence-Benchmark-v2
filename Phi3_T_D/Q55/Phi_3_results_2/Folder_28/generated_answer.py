def lists_with_product_equal_n(circular_list, n=85):
    length = len(circular_list)
    product_sublists = []
    for size in range(1, length + 1):
        for start in range(length):
            end = (start + size - 1) % length
            if end < start:
                break
            sublist = circular_list[start:end + 1] + circular_list[:start]
            if len(sublist) > size:
                sublist = sublist[size:]
            if sublist[0] == 0 or n % sublist[0] != 0:
                continue
            temp_n = n
            for num in sublist:
                if temp_n % num != 0:
                    break
                temp_n //= num
            else:
                product_sublists.append(sublist)
    return product_sublists