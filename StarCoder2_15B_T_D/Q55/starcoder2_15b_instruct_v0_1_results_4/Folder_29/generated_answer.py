def lists_with_product_equal_n(numbers):
    result = []
    product = 1
    sublist = []
    size = len(numbers)
    i = 0
    while i < size:
        product = 1
        sublist = []
        j = i
        while j < i + size and product != 15 and (len(sublist) <= size):
            product *= numbers[j % size]
            sublist.append(numbers[j % size])
            j += 1
        if product == 15:
            result.append(sublist)
        i += 1
    return result