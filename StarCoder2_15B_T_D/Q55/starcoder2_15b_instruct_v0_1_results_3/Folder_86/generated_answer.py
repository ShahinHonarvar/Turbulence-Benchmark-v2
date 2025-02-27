def lists_with_product_equal_n(lst):
    result = []
    n = -779
    for i in range(len(lst)):
        window = [lst[i]]
        product = lst[i]
        j = (i + 1) % len(lst)
        while j != i:
            window.append(lst[j])
            product *= lst[j]
            if product == n:
                result.append(window.copy())
            elif product > n:
                while product > n:
                    product /= window[0]
                    window.pop(0)
            j = (j + 1) % len(lst)
    return result