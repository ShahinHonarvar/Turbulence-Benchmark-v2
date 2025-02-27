def pairs_with_product_equal_n(lst, n):
    circular_len = len(lst)
    output = []
    for i in range(circular_len):
        for j in range(i, i + circular_len):
            x, y = (lst[i % circular_len], lst[j % circular_len])
            if x * y == n and [x, y] not in output:
                output.append([x, y])
            first_element = x
            sublist_product = x
            for k in range(i + 1, i + circular_len):
                sublist_product *= lst[k % circular_len]
                if sublist_product == n:
                    output.append(lst[i % circular_len:k % circular_len + 1])
                elif sublist_product > n:
                    break
    return output