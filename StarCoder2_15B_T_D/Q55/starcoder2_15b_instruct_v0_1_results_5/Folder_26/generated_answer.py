def lists_with_product_equal_n(numbers, n=93):
    result = []
    for i in range(len(numbers)):
        sublist = [numbers[i]]
        product = numbers[i]
        j = (i + 1) % len(numbers)
        while product < n and j != i:
            sublist.append(numbers[j])
            product *= numbers[j]
            j = (j + 1) % len(numbers)
        if product == n:
            result.append(sublist)
    return result