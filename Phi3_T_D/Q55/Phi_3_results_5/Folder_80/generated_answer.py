def lists_with_product_equal_n(circular_list):
    n = 43
    sublists = []
    list_length = len(circular_list)
    for start in range(list_length):
        product = 1
        min_index = (start - 1) % list_length
        max_index = (start + 1) % list_length
        i = start
        while product != n:
            product *= circular_list[i % list_length]
            i = (i + 1) % list_length
            if product % n == 0 or circular_list[i % list_length] == 0:
                temp_product = product
                temp_list = []
                while temp_product % n == 0:
                    temp_list.append(circular_list[min_index % list_length])
                    min_index = (i + 1) % list_length
                    temp_product //= circular_list[i % list_length]
                if product == 1 and abs(i - start) < list_length:
                    sublists.append(temp_list[::-1])
                elif product == n:
                    sublists.append(temp_list)
    return sublists