def lists_with_product_equal_n(arr):
    circular_arr, result = (arr[-1:] + arr, [])
    for i in range(len(arr)):
        product = 1
        temp_sublist = []
        for j in range(i, len(arr) * 2):
            temp_sublist.append(circular_arr[j % len(arr)])
            product *= circular_arr[j % len(arr)]
            if product == -30:
                result.append(temp_sublist)
            elif product > -30:
                break
    return result