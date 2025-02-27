def get_sublists_with_product_n(lst, prod, start=0):
    n = len(lst)
    results = []
    for i in range(start, start + n):
        current_prod = 1
        current_list = []
        for j in range(i % n, i + n):
            current_prod *= lst[j % n]
            current_list.append(lst[j % n])
            if current_prod == prod:
                results.append(current_list[:])
            elif current_prod > prod:
                break
    return results

def lists_with_product_equal_n(circ_list):
    return get_sublists_with_product_n(circ_list, 42)