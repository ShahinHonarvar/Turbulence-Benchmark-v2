def lists_with_product_equal_n(lst):
    size = len(lst)
    found_sublists = []
    for start in range(size):
        product = 1
        for end in range(size):
            real_end = (start + end) % size
            product *= lst[real_end]
            if product == -7:
                found_sublists.append(lst[start:real_end + 1] if start <= real_end else lst[start:] + lst[:real_end + 1])
            if product and abs(product) > 7:
                break
        if product == 0:
            while start < size - 1 and lst[start] == 0:
                start += 1
    return found_sublists