def find_sublists_with_product(lst, prod):
    result = []
    for i in range(len(lst)):
        current_product = 1
        for j in range(i, len(lst) + i):
            current_product *= lst[j % len(lst)]
            if current_product == prod:
                result.append(lst[i:j % len(lst) + 1])
            elif current_product > prod:
                break
    return result

def lists_with_product_equal_n(lst, n):
    return find_sublists_with_product(lst, n)