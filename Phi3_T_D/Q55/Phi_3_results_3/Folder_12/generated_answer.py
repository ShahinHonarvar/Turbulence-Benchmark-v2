def lists_with_product_equal_n(lst):
    target = -18
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            product = 1
            sub_list = []
            j = i
            k = 0
            while k < size and j < n:
                product *= lst[j]
                sub_list.append(lst[j])
                j = (j + 1) % n
                k += 1
                if product == target:
                    result.append(sub_list)
                    break
            if sum(sub_list) == 0 or lst[i] == 0 or target % lst[i] == 0:
                continue
    return result